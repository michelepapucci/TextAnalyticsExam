import sys
sys.path.insert(0, '../')

from libraries.Experiment.experiment import NLMExperiment
from libraries.Experiment.metrics import Metrics
from libraries.Experiment.utils import gender_to_int


def main(model_folder):
    experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "../src/data/post_processed/training_filtered.csv",
                               'accuracy')
    experiment.process_dataset(functions_to_map=[gender_to_int], to_drop=['Age', 'Id', 'Topic'],
                               to_rename={'Gender': 'label', 'Sentence': 'sentence'})
    experiment.load_model(model_folder)

    experiment.set_test_dataset("../src/data/post_processed/test_1_filtered.csv", functions_to_map=[gender_to_int],
                                to_drop=['Age', 'Id', 'Topic'],
                                to_rename={'Gender': 'label', 'Sentence': 'sentence'})

    experiment.test(experiment.test_dataset['test'], "../output/bert_for_gender_predictions.tsv")
    m = Metrics("../output/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("../output/")


if __name__ == '__main__':
    main("../models/gender_single_label")
