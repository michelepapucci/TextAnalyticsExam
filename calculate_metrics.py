from src.libraries.experiment import NLMExperiment
from src.libraries.metrics import Metrics
from src.libraries.utils import gender_to_int


def main(model_folder):
    m = Metrics("output/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("output/")

    '''experiment = NLMExperiment("dbmdz/bert-base-italian-cased", "src/data/post_processed/training_filtered.csv",
                                   'accuracy')
        experiment.process_dataset(functions_to_map=[gender_to_int], to_drop=['Age', 'Id', 'Topic'],
                                   to_rename={'Gender': 'label', 'Sentence': 'sentence'})
        experiment.load_model(model_folder)
    
        experiment.test(experiment.dataset['val'], "output/bert_for_gender_predictions.tsv")'''


if __name__ == '__main__':
    main("models/gender_single_label")
