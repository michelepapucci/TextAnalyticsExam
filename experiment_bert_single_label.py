from libraries.Experiment.experiment import NLMExperiment
from libraries.Experiment.metrics import Metrics
from libraries.Experiment.utils import gender_to_int, topic_to_int, age_range_to_int


def gender():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                               'accuracy', load_weight=False)
    experiment.process_dataset(functions_to_map=[gender_to_int], to_drop=['Age', 'Id', 'Topic'],
                               to_rename={'Gender': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    model_folder = "models/bert_gender_config/"

    experiment.save_model(model_folder)

    experiment.load_model(model_folder)

    experiment.set_test_dataset("src/data/post_processed/test_1_filtered.csv", functions_to_map=[gender_to_int],
                                to_drop=['Age', 'Id', 'Topic'],
                                to_rename={'Gender': 'label', 'Sentence': 'sentence'})

    experiment.test(experiment.test_dataset['test'], f"output/{model_folder}output.tsv")

    m = Metrics(f"output/{model_folder}output.tsv",
                ['Uomo', 'Donna'])
    m.report(f"output/{model_folder}classification_report.txt")


def topic():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                               'accuracy', load_weight=False, num_labels=11)
    experiment.process_dataset(functions_to_map=[topic_to_int], to_drop=['Age', 'Id', 'Gender'],
                               to_rename={'Topic': 'label', 'Sentence': 'sentence'})
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    model_folder = "models/bert_topic_config/"

    experiment.save_model(model_folder)

    experiment.load_model(model_folder)

    experiment.set_test_dataset("src/data/post_processed/test_1_filtered.csv", functions_to_map=[topic_to_int],
                                to_drop=['Age', 'Id', 'Gender'],
                                to_rename={'Topic': 'label', 'Sentence': 'sentence'})

    experiment.test(experiment.test_dataset['test'], f"output/{model_folder}output.tsv")

    m = Metrics(f"output/{model_folder}output.tsv",
                ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS',
                 'METAL-DETECTING',
                 'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY'])
    m.report(f"output/{model_folder}classification_report.txt")


def age():
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                               'accuracy', load_weight=False, num_labels=5,)
    experiment.process_dataset(functions_to_map=[age_range_to_int], to_drop=['Topic', 'Id', 'Gender'],
                               to_rename={'Age': 'label', 'Sentence': 'sentence'})
    print(experiment.dataset)
    experiment.fine_tune()
    experiment.evaluate()
    print(experiment.evaluation_results)

    model_folder = "models/bert_age_config/"

    experiment.save_model(model_folder)

    experiment.load_model(model_folder)

    experiment.set_test_dataset("src/data/post_processed/test_1_filtered.csv", functions_to_map=[age_range_to_int],
                                to_drop=['Topic', 'Id', 'Gender'],
                                to_rename={'Age': 'label', 'Sentence': 'sentence'})

    experiment.test(experiment.test_dataset['test'], f"output/{model_folder}output.tsv")

    m = Metrics(f"output/{model_folder}output.tsv",
                ["0-19", "20-29", "30-39", "40-49", "50-100"])
    m.report(f"output/{model_folder}classification_report.txt")


def main():
    # gender()
    # topic()
    age()


if __name__ == '__main__':
    main()
