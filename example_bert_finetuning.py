from src.libraries.experiment import NLMExperiment


def gender_to_int(row):
    if row['Gender'] == 'M':
        row['Gender'] = 0
    else:
        row['Gender'] = 1
    return row


def main():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[gender_to_int], to_drop=['Age', 'Id', 'Topic'],
                               to_rename={'Gender': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    experiment.test(experiment.dataset['val'], "output/bert_for_gender_predictions.tsv")


if __name__ == '__main__':
    main()
