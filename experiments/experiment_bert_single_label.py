from libraries.Experiment.experiment import NLMExperiment
from libraries.Experiment.metrics import Metrics


def gender_to_int(row):
    if row['Gender'] == 'M':
        row['Gender'] = 0
    else:
        row['Gender'] = 1
    return row


def topic_to_int(row):
    pass


def age_range_to_int(row):
    pass


def gender():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "../src/data/post_processed/training_filtered.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[gender_to_int], to_drop=['Age', 'Id', 'Topic'],
                               to_rename={'Gender': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    experiment.test(experiment.dataset['val'], "output/bert_for_gender_predictions.tsv")
    m = Metrics("../output/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("output/")


def topic():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "../src/data/post_processed/training_filtered.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[topic_to_int], to_drop=['Age', 'Id', 'Gender'],
                               to_rename={'Topic': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    experiment.test(experiment.dataset['val'], "output/bert_for_topic_predictions.tsv")
    m = Metrics("../output/bert_for_gender_predictions.tsv", [])  # TODO
    m.report("output/")


def age():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "../src/data/post_processed/training_filtered.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[age_range_to_int], to_drop=['Topic', 'Id', 'Gender'],
                               to_rename={'Age': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    experiment.test(experiment.dataset['val'], "output/bert_for_gender_predictions.tsv")
    m = Metrics("../output/bert_for_age_predictions.tsv", [])  # TODO
    m.report("output/")


def main():
    gender()
    topic()
    age()


if __name__ == '__main__':
    main()
