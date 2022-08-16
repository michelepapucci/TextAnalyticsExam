from src.libraries.metrics import Metrics


def main():
    m = Metrics("output/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("output/")


if __name__ == '__main__':
    main()
