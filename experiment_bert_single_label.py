from libraries.Experiment.experiment import NLMExperiment
from libraries.Experiment.metrics import Metrics
from libraries.Experiment.utils import gender_to_int, topic_to_int, age_range_to_int


def gender():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/bert_shots/training_1_shot.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[gender_to_int], to_drop=['Age', 'Id', 'Topic'],
                               to_rename={'Gender': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    model_folder = "models/bert_gender_single_label_1_shot/"

    experiment.save_model(model_folder)

    experiment.load_model(model_folder)

    experiment.set_test_dataset("src/data/post_processed/test_1_filtered.csv", functions_to_map=[gender_to_int],
                                to_drop=['Age', 'Id', 'Topic'],
                                to_rename={'Gender': 'label', 'Sentence': 'sentence'})

    experiment.test(experiment.test_dataset['test'], f"output/{model_folder}output.tsv")

    m = Metrics("../output/topic/bert_for_topic_predictions.tsv",
                ['Uomo', 'Donna'])
    m.report(f"output/{model_folder}classification_report.txt")


def topic():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                               'accuracy', num_labels=11)
    experiment.process_dataset(functions_to_map=[topic_to_int], to_drop=['Age', 'Id', 'Gender'],
                               to_rename={'Topic': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    experiment.save_model("models/bert_topic_single_label/")


def age():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                               'accuracy', num_labels=5)
    experiment.process_dataset(functions_to_map=[age_range_to_int], to_drop=['Topic', 'Id', 'Gender'],
                               to_rename={'Age': 'label', 'Sentence': 'sentence'})
    print(experiment.dataset)
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    experiment.save_model("models/bert_age_single_label/")


def main():
    gender()
    # topic()
    # age()


if __name__ == '__main__':
    main()
