import pandas as pd
import json


def gender_to_word(row):
    if row == 'M':
        return "uomo"
    else:
        return "donna"


def topic_to_word(row):
    if row == 'ANIME':
        return "anime"
    if row == 'AUTO-MOTO':
        return "automobilismo"
    if row == 'BIKES':
        return "bici"
    if row == 'SPORTS':
        return "sport"
    if row == 'NATURE':
        return "natura"
    if row == 'METAL-DETECTING':
        return "metalli"
    if row == 'MEDICINE-AESTHETICS':
        return "medicina"
    if row == 'CELEBRITIES':
        return "celebrità"
    if row == 'SMOKE':
        return "fumo"
    if row == 'ENTERTAINMENT':
        return "intrattenimento"
    if row == 'TECHNOLOGY':
        return "tecnologia"


def to_json(df, column_to_generate, iteration, map_function=None):
    if map_function is not None:
        df[column_to_generate] = df[column_to_generate].map(map_function)
    with open(f"jsons/{column_to_generate}_{iteration}.json", "w") as output:
        for index, row in df.iterrows():
            output.write(json.dumps({"translation": {"s": row['Sentence'], "t": row[column_to_generate]}}))
            output.write("\n")


if __name__ == '__main__':
    tasks = ['Topic', 'Gender', 'Age']
    functions = {
        'Topic': topic_to_word,
        'Gender': gender_to_word,
        'Age': None,
    }
    for task in tasks:
        datasets = ['training_1_shot.csv', 'training_2_shot.csv', 'training_3_shot.csv', 'training_4_shot.csv']
        for index, dataset in enumerate(datasets):
            temp = pd.read_csv(dataset)
            if index != 0:
                df = df.append(temp, ignore_index=True)
            else:
                df = temp
            to_json(df, task, index, functions[task])
