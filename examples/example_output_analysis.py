import sys
sys.path.insert(0, '../')

from libraries.Experiment.metrics import Metrics


def main():
    m = Metrics("MultiTaskBert/3_out/topic_predictions_1.tsv", ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS', 'METAL-DETECTING',
              'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY'])
    m.report("output/bert_multitask_gender/")


if __name__ == '__main__':
    main()
