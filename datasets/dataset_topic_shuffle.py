from datasets import load_dataset, DatasetDict, load_metric
import json


def topic_to_word(row):
    if row['Topic'] == 'ANIME':
        row['Topic'] = "sport"
    if row['Topic'] == 'AUTO-MOTO':
        row['Topic'] = "celebrità"
    if row['Topic'] == 'BIKES':
        row['Topic'] = "medicina"
    if row['Topic'] == 'SPORTS':
        row['Topic'] = "tecnologia"
    if row['Topic'] == 'NATURE':
        row['Topic'] = "metalli"
    if row['Topic'] == 'METAL-DETECTING':
        row['Topic'] = "intrattenimento"
    if row['Topic'] == 'MEDICINE-AESTHETICS':
        row['Topic'] = "fumo"
    if row['Topic'] == 'CELEBRITIES':
        row['Topic'] = "bici"
    if row['Topic'] == 'SMOKE':
        row['Topic'] = "natura"
    if row['Topic'] == 'ENTERTAINMENT':
        row['Topic'] = "anime"
    if row['Topic'] == 'TECHNOLOGY':
        row['Topic'] = "automobilismo"
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
                              functions_to_map=[topic_to_word],
                              to_drop=['Age', 'Id', 'Gender'],
                              to_rename={'Topic': 'labels', 'Sentence': 'sentence'})
    list_of_sentences = []
    for row in dataset['train']:
        list_of_sentences.append({"translation": {"s": row['sentence'], "t": row['labels']}})
    with open("dataset_topic_shuffle.json", "a") as output:
        for row in dataset['train']:
            output.write(json.dumps({"translation": {"s": row['sentence'], "t": row['labels']}}))
            output.write("\n")


if __name__ == "__main__":
    main()