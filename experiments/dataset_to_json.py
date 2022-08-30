from datasets import load_dataset, DatasetDict, load_metric
import json


def gender_to_word(row):
    if row['Gender'] == 'M':
        row['Gender'] = "uomo"
    else:
        row['Gender'] = "donna"
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
    dataset = process_dataset("../src/data/post_processed/training_filtered.csv",
                              functions_to_map=[gender_to_word],
                              to_drop=['Age', 'Id', 'Topic'],
                              to_rename={'Gender': 'labels', 'Sentence': 'sentence'})

    with open("dataset.json", "a") as output:
        for row in dataset['train']:
            output.write(json.dumps({"translation": {"s": row['sentence'], "t": row['labels']}}))
            output.write("\n")


if __name__ == "__main__":
    main()
