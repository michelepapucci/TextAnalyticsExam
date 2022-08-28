import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer, \
    DataCollatorForSeq2Seq
from datasets import load_dataset, DatasetDict, load_metric
import torch
import numpy as np

model_name = "gsarti/it5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
metric = load_metric("rouge")


def model_init():
    return AutoModelForSeq2SeqLM.from_pretrained(model_name)


def load_from_csv(dataset_path):
    return load_dataset('csv', data_files=dataset_path)


def tokenize_function(row):
    return tokenizer(row['Sentence'], truncation=True)


def preprocess_output_label(examples, target):
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples[target], truncation=True)
    return labels["input_ids"]


def gender_to_word(row):
    if row['Gender'] == 'M':
        row['Gender'] = "uomo"
    else:
        row['Gender'] = "donna"
    print(row['Gender'])
    return row


def gender_to_int(row):
    with tokenizer.as_target_tokenizer():
        tokenized = tokenizer(row['Gender'], truncation=True)
    row['Gender'] = tokenized["input_ids"]
    return row


def topic_to_int(row):
    with tokenizer.as_target_tokenizer():
        tokenized = tokenizer(row['Topic'], padding="max_length", truncation=True)
    row['Topic'] = tokenized["input_ids"]
    return row

def load_from_csv(dataset_path):
    return load_dataset('csv', data_files=dataset_path)


def process_dataset(dataset_path, functions_to_map=None, to_rename={}, to_drop=[]):
    raw = load_from_csv(dataset_path)
    d = raw['train'].train_test_split(0.2)
    dataset = DatasetDict({'train': d['train'], 'validation': d['test']})  # TODO: Guardare bene
    if functions_to_map is not None:
        for function in functions_to_map:
            dataset = dataset.map(function)
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    renamed_d = tokenized_dataset.rename_columns(to_rename)
    removed_d = renamed_d.remove_columns(to_drop)
    dataset = removed_d
    return dataset


def prefix_classify_gender(row):
    row['Sentence'] = 'Classifica genere: ' + row['Sentence']
    return row


def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)

    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Rouge expects a newline after each sentence
    decoded_preds = ["\n".join(nltk.sent_tokenize(pred.strip()))
                     for pred in decoded_preds]
    decoded_labels = ["\n".join(nltk.sent_tokenize(label.strip()))
                      for label in decoded_labels]

    # Compute ROUGE scores
    result = metric.compute(predictions=decoded_preds, references=decoded_labels,
                            use_stemmer=True)

    # Extract ROUGE f1 scores
    result = {key: value.mid.fmeasure * 100 for key, value in result.items()}

    # Add mean generated length to metrics
    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id)
                       for pred in predictions]
    result["gen_len"] = np.mean(prediction_lens)

    return {k: round(v, 4) for k, v in result.items()}


def print_dataset(dataset):
    print(dataset)
    i = 0
    for row in dataset['train']:
        i = i + 1
        if i == 10:
            break
        print(f"{row['sentence']} - {row['input_ids']} - {row['labels']}")


def main():
    data_collator = DataCollatorForSeq2Seq(tokenizer)
    dataset = process_dataset("../src/data/post_processed/training_filtered.csv",
                              functions_to_map=[prefix_classify_gender, gender_to_word, gender_to_int],
                              to_drop=['Age', 'Id', 'Topic'],
                              to_rename={'Gender': 'labels', 'Sentence': 'sentence'})
    print_dataset(dataset)

    batch_size = 8

    model_dir = "../models/it5"

    args = Seq2SeqTrainingArguments(
        model_dir,
        # evaluation_strategy="steps",
        # eval_steps=400,
        learning_rate=4e-5,
        # save_strategy="steps",
        # save_steps=400,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=2,
        predict_with_generate=True,
        fp16=True,
        # load_best_model_at_end=True,
        metric_for_best_model="rouge1", )

    trainer = Seq2SeqTrainer(
        model_init=model_init,
        args=args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        data_collator=data_collator,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics
    )

    trainer.train()
    trainer.save_model(model_dir + "models/it5/final_model")


def test():
    model_dir = "../models/it5/checkpoint-2500/"

    text = """Classifica genere: Amici dove posso scambiar due chiacchiere con qualcuno sul GULP ? Questo forum va bene? Ciao !"""

    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

    inputs = [text]

    inputs = tokenizer(inputs, truncation=True, padding=True, return_tensors="pt")
    output = model.generate(**inputs, do_sample=True)

    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    print(decoded_output)


if __name__ == '__main__':
    main()
    test()
