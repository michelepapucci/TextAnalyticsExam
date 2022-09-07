import math
from typing import Optional, Union, Tuple, Any, List, Dict, Mapping

import numpy as np
import torch
from attr import dataclass
from datasets import load_dataset
from torch.nn import CrossEntropyLoss
from torch import nn
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import BertPreTrainedModel, BertModel, AutoTokenizer, training_args, TrainingArguments, Trainer, \
    get_scheduler
from transformers.data.data_collator import DataCollatorMixin, default_data_collator, InputDataClass
from transformers.utils import ModelOutput
import evaluate
from accelerate import Accelerator


@dataclass
class MultiTaskDataCollator(DataCollatorMixin):

    def __call__(self, features: List[Dict[str, Any]], return_tensors=None) -> Dict[str, Any]:
        return torch_default_data_collator(features)


def torch_default_data_collator(features: List[InputDataClass]) -> Dict[str, Any]:
    if not isinstance(features[0], Mapping):
        features = [vars(f) for f in features]
    first = features[0]
    batch = {}

    if "gender_labels" in first and first["gender_labels"] is not None:
        label = first["gender_labels"].item() if isinstance(first["gender_labels"], torch.Tensor) else first[
            "gender_labels"]
        dtype = torch.long if isinstance(label, int) else torch.float
        batch["gender_labels"] = torch.tensor([f["gender_labels"] for f in features], dtype=dtype)
    if "topic_labels" in first and first["topic_labels"] is not None:
        label = first["topic_labels"].item() if isinstance(first["topic_labels"], torch.Tensor) else first[
            "topic_labels"]
        dtype = torch.long if isinstance(label, int) else torch.float
        batch["topic_labels"] = torch.tensor([f["topic_labels"] for f in features], dtype=dtype)
    if "age_labels" in first and first["age_labels"] is not None:
        label = first["age_labels"].item() if isinstance(first["age_labels"], torch.Tensor) else first["age_labels"]
        dtype = torch.long if isinstance(label, int) else torch.float
        batch["age_labels"] = torch.tensor([f["age_labels"] for f in features], dtype=dtype)

    for k, v in first.items():
        if k not in ("label", "label_ids") and v is not None and not isinstance(v, str):
            if isinstance(v, torch.Tensor):
                batch[k] = torch.stack([f[k] for f in features])
            else:
                batch[k] = torch.tensor([f[k] for f in features])

    return batch


class MultiTaskSequenceClassifierOutput(ModelOutput):
    loss: Optional[torch.FloatTensor] = None
    gender_logits: torch.FloatTensor = None
    topic_logits: torch.FloatTensor = None
    age_logits: torch.FloatTensor = None
    hidden_states: Optional[Tuple[torch.FloatTensor]] = None
    attentions: Optional[Tuple[torch.FloatTensor]] = None


class BertMultiTaskForSequenceClassification(BertPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.config = config

        self.bert = BertModel(config)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)

        self.gender_classifier = nn.Linear(config.hidden_size, 2)
        self.topic_classifier = nn.Linear(config.hidden_size, 11)
        self.age_classifier = nn.Linear(config.hidden_size, 5)

        # Initialize weights and apply final processing
        self.post_init()

    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None,
                token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None,
                head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None,
                gender_labels: Optional[torch.Tensor] = None, topic_labels: Optional[torch.Tensor] = None,
                age_labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None,
                output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, ):
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        pooled_output = outputs[1]

        pooled_output = self.dropout(pooled_output)
        gender_logits = self.gender_classifier(pooled_output)
        topic_logits = self.topic_classifier(pooled_output)
        age_logits = self.age_classifier(pooled_output)

        loss = 0.0
        loss_fct = CrossEntropyLoss()
        loss += loss_fct(gender_logits, gender_labels)
        loss += loss_fct(topic_logits, topic_labels)
        loss += loss_fct(age_logits, age_labels)

        return MultiTaskSequenceClassifierOutput(
            loss=loss,
            gender_logits=gender_logits,
            topic_logits=topic_logits,
            age_logits=age_logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )


def compute_metrics(self, eval_pred):
    print(eval_pred)
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return self.metric.compute(predictions=predictions, references=labels)


if __name__ == '__main__':

    model_name = "dbmdz/bert-base-italian-cased"
    output_dir = "models/"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    dataset_path = "training_filtered.csv"


    def tokenize_function(row):
        return tokenizer(row['Sentence'], padding="max_length", truncation=True, max_length=128)


    def gender_to_int(row):
        if row['Gender'] == 'M':
            row['Gender'] = 0
        else:
            row['Gender'] = 1
        return row


    def topic_to_int(row):
        topics = ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS',
                  'METAL-DETECTING',
                  'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY']
        if row['Topic'] in topics:
            row['Topic'] = topics.index(row['Topic'])
        else:
            print("Error!")
        return row


    def age_range_to_int(row):
        ages = ["0-19", "20-29", "30-39", "40-49", "50-100"]
        if row['Age'] in ages:
            row['Age'] = ages.index(row['Age'])
        else:
            print("Porcodio")
        return row


    ''' if training_args is None and training_args is None:
         training_args = TrainingArguments(output_dir=output_dir)
         training_args.num_train_epochs = float(2)
         training_args.save_strategy = 'no'
         training_args.learning_rate = 0.00002

     trainer = Trainer(
         model=model,
         args=training_args,
         train_dataset=dataset['train'],
         compute_metrics=compute_metrics,
     )

     trainer.train()'''

    dataset = load_dataset('csv', data_files=dataset_path)
    dataset = dataset.map(gender_to_int)
    dataset = dataset.map(topic_to_int)
    dataset = dataset.map(age_range_to_int)
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    renamed_d = tokenized_dataset.rename_columns(
        {'Gender': 'gender_labels', 'Topic': 'topic_labels', 'Age': 'age_labels'})
    removed_d = renamed_d.remove_columns(['Id', 'Sentence'])
    dataset = removed_d

    test_dataset = load_dataset('csv', data_files="test_1_filtered.csv")
    test_dataset = test_dataset.map(gender_to_int)
    test_dataset = test_dataset.map(topic_to_int)
    test_dataset = test_dataset.map(age_range_to_int)
    tokenized_dataset = test_dataset.map(tokenize_function, batched=True)
    renamed_d = tokenized_dataset.rename_columns(
        {'Gender': 'gender_labels', 'Topic': 'topic_labels', 'Age': 'age_labels'})
    removed_d = renamed_d.remove_columns(['Id', 'Sentence'])
    test_dataset = removed_d

    model = BertMultiTaskForSequenceClassification.from_pretrained(model_name)

    accelerator = (
        Accelerator()
    )

    data_collator = MultiTaskDataCollator()

    train_dataloader = DataLoader(dataset['train'], shuffle=True, collate_fn=data_collator, batch_size=8)
    eval_dataloader = DataLoader(test_dataset['train'], shuffle=True, collate_fn=data_collator, batch_size=8)

    no_decay = ["bias", "LayerNorm.weight"]
    optimizer_grouped_parameters = [
        {
            "params": [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
            "weight_decay": 0.0,
        },
        {
            "params": [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)],
            "weight_decay": 0.0,
        },
    ]
    optimizer = torch.optim.AdamW(optimizer_grouped_parameters, lr=0.00002)
    num_epochs = 2
    lr_scheduler = get_scheduler(
        name="linear",
        optimizer=optimizer,
        num_warmup_steps=0,
        num_training_steps=num_epochs * len(train_dataloader),
    )

    # Prepare everything with our `accelerator`.
    model, optimizer, train_dataloader, eval_dataloader, lr_scheduler = accelerator.prepare(
        model, optimizer, train_dataloader, eval_dataloader, lr_scheduler
    )

    age_metric = evaluate.load("accuracy")
    topic_metric = evaluate.load("accuracy")
    gender_metric = evaluate.load("accuracy")

    total_batch_size = 8
    progress_bar = tqdm(range(num_epochs * len(train_dataloader)), disable=not accelerator.is_local_main_process)
    completed_steps = 0

    for epoch in range(num_epochs):
        with open(f'output/age_predictions_{epoch}.tsv', 'w') as age_prediction_file:
            age_prediction_file.write("y_true\ty_pred\n")
        with open(f'output/topic_predictions_{epoch}.tsv', 'w') as topic_prediction_file:
            topic_prediction_file.write("y_true\ty_pred\n")
        with open(f'output/gender_predictions_{epoch}.tsv', 'w') as gender_prediction_file:
            gender_prediction_file.write("y_true\ty_pred\n")
        model.train()
        for step, batch in enumerate(train_dataloader):
            outputs = model(**batch)
            loss = outputs.loss
            accelerator.backward(loss)
            optimizer.step()
            lr_scheduler.step()
            optimizer.zero_grad()
            progress_bar.update(1)
            completed_steps += 1

        model.eval()
        samples_seen = 0
        for step, batch in enumerate(eval_dataloader):
            with torch.no_grad():
                outputs = model(**batch)

            age_predictions = outputs.age_logits.argmax(dim=-1)
            age_predictions, age_references = accelerator.gather((age_predictions, batch["age_labels"]))
            with open(f'output/age_predictions_{epoch}.tsv', 'a') as output_file:
                for pred, ref in zip(age_predictions, age_references):
                    output_file.write(f"{ref}\t{pred}\n")
            age_metric.add_batch(
                predictions=age_predictions,
                references=age_references,
            )

            gender_predictions = outputs.gender_logits.argmax(dim=-1)
            gender_predictions, gender_references = accelerator.gather((gender_predictions, batch["gender_labels"]))
            with open(f'output/gender_predictions_{epoch}.tsv', 'a') as output_file:
                for pred, ref in zip(gender_predictions, gender_references):
                    output_file.write(f"{ref}\t{pred}\n")
            gender_metric.add_batch(
                predictions=gender_predictions,
                references=gender_references,
            )

            topic_predictions = outputs.topic_logits.argmax(dim=-1)
            topic_predictions, topic_references = accelerator.gather((topic_predictions, batch["topic_labels"]))
            with open(f'output/topic_predictions_{epoch}.tsv', 'a') as output_file:
                for pred, ref in zip(topic_predictions, topic_references):
                    output_file.write(f"{ref}\t{pred}\n")
            topic_metric.add_batch(
                predictions=topic_predictions,
                references=topic_references,
            )

        age_eval_metric = age_metric.compute()
        gender_eval_metric = gender_metric.compute()
        topic_eval_metric = topic_metric.compute()

        print(f"age accuracy: {age_eval_metric}")
        print(f"gender accuracy: {gender_eval_metric}")
        print(f"topic accuracy: {topic_eval_metric}")

    accelerator.wait_for_everyone()
    unwrapped_model = accelerator.unwrap_model(model)
    unwrapped_model.save_pretrained(
        output_dir, is_main_process=accelerator.is_main_process, save_function=accelerator.save
    )
    if accelerator.is_main_process:
        tokenizer.save_pretrained(output_dir)
