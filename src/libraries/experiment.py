from transformers import AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset, DatasetDict, load_metric
import numpy as np
from transformers import AutoModelForSequenceClassification


class NLMExperiment:

    def __init__(self, model_name, dataset_path, metrics):
        self.metric = load_metric(metrics)
        self.model_name = model_name
        self.dataset_path = dataset_path

        self.dataset = None
        self.trainer = None
        self.test_results = None
        self.evaluation_results = None
        self.training_args = None

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def load_from_csv(self):
        return load_dataset('csv', data_files=self.dataset_path)

    def tokenize_function(self, row):
        return self.tokenizer(row['Sentence'], padding="max_length", truncation=True, max_length=128)

    def process_dataset(self, functions_to_map=None, to_rename={}, to_drop=[]):

        raw = self.load_from_csv()
        test = raw['train'].train_test_split(0.2)
        dataset = DatasetDict({'train': raw['train'], 'val': test['test']})
        if functions_to_map is not None:
            for function in functions_to_map:
                dataset = dataset.map(function)
        tokenized_dataset = dataset.map(self.tokenize_function, batched=True)
        renamed_d = tokenized_dataset.rename_columns(to_rename)
        removed_d = renamed_d.remove_columns(to_drop)
        self.dataset = removed_d

    def compute_metrics(self, eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return self.metric.compute(predictions=predictions, references=labels)

    def fine_tune(self, training_args=None, output_dir="output/"):
        if training_args is None and self.training_args is None:
            self.training_args = TrainingArguments(output_dir=output_dir)
            self.training_args.num_train_epochs = float(2)
            self.training_args.save_strategy = 'no'
            self.training_args.learning_rate = 0.00002

        self.trainer = Trainer(
            model=self.model,
            args=self.training_args,
            train_dataset=self.dataset['train'],
            eval_dataset=self.dataset['val'],
            compute_metrics=self.compute_metrics
        )

        self.trainer.train()

    def evaluate(self):
        self.evaluation_results = self.trainer.evaluate()

    def test(self, dataset_to_test, path_to_file=False):
        self.test_results = self.trainer.predict(dataset_to_test)
        if path_to_file:
            with open(path_to_file, 'w') as output:
                output.write("y_true\ty_proba\ty_pred\n")
                predictions = self.test_results.predictions
                predicted_classes = np.argmax(predictions, axis=-1)
                for y_true, y_proba, y_pred in zip(self.test_results.label_ids, predicted_classes):
                    output.write(str(y_true) + '\t' + str(y_proba) + str(y_pred) + '\n')
