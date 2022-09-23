from datasets import load_dataset, DatasetDict, load_metric
import json


def age_shuffled(row):
    if row['Age'] == '0-19':
        row['Age'] = "40-49"
    if row['Age'] == '20-29':
        row['Age'] = "50-100"
    if row['Age'] == '30-39':
        row['Age'] = "0-19"
    if row['Age'] == '40-49':
        row['Age'] = "20-29"
    if row['Age'] == '50-100':
        row['Age'] = "30-39"
    return row


def load_from_csv(dataset_path):
    return load_dataset('csv', data_files=dataset_path)


def process_dataset(dataset_path, functions_to_map=None, to_rename={}, to_drop=[]):
    raw = load_from_csv(dataset_path)
    d = raw['train'].train_test_split(0.2)
    dataset = DatasetDict({'train': d['train'], 'validation': d['test']})
    if functions_to_map is not None:
        for function in functions_to_map:
            dataset = dataset.map(function)
    tokenized_dataset = dataset  # dataset.map(tokenize_function, batched=True)
    renamed_d = tokenized_dataset.rename_columns(to_rename)
    removed_d = renamed_d.remove_columns(to_drop)
    dataset = removed_d
    return dataset


def main():
    dataset = process_dataset("training_filtered.csv",
                              functions_to_map=[age_shuffled],
                              to_drop=['Topic', 'Id', 'Gender'],
                              to_rename={'Age': 'labels', 'Sentence': 'sentence'})
    list_of_sentences = []
    for row in dataset['train']:
        list_of_sentences.append({"translation": {"s": row['sentence'], "t": row['labels']}})
    with open("dataset_age_shuffled.json", "a") as output:
        for row in dataset['train']:
            output.write(json.dumps({"translation": {"s": row['sentence'], "t": row['labels']}}))
            output.write("\n")


if __name__ == "__main__":
    main()