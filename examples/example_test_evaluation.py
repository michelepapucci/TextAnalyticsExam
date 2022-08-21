import sys

sys.path.insert(0, '../')

from libraries.Experiment.experiment import NLMExperiment
from libraries.Experiment.metrics import Metrics
from libraries.Experiment.utils import gender_to_int, topic_to_int


def main(model_folder):
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "../src/data/post_processed/training_filtered.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[topic_to_int], to_drop=['Age', 'Id', 'Gender'],
                               to_rename={'Topic': 'label', 'Sentence': 'sentence'})
    experiment.load_model(model_folder)

    experiment.set_test_dataset("../src/data/post_processed/test_1_filtered.csv", functions_to_map=[topic_to_int],
                                to_drop=['Age', 'Id', 'Gender'],
                                to_rename={'Topic': 'label', 'Sentence': 'sentence'})

    experiment.test(experiment.test_dataset['test'], "../output/topic/bert_for_topic_predictions.tsv")
    m = Metrics("../output/topic/bert_for_topic_predictions.tsv",
                ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS',
                 'METAL-DETECTING', 'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY'])
    m.report("../output/topic/")


if __name__ == '__main__':
    main("../models/bert_topic_single_label/")
