from sklearn.metrics import classification_report
import pandas as pd


def main(prediction_file, labels):
    df = pd.read_csv(prediction_file, sep="\t", header=0)
    with open(f"{prediction_file.split(',')[0]}_classification_report.txt", "w") as output:
        cr = classification_report(df['y_true'].values, df['y_pred'].values, labels=[i for i in range(len(labels))],
                                   target_names=labels)
        print(cr)
        output.write(cr)


if __name__ == '__main__':
    main("age_predictions_1.tsv", ["0-19", "20-29", "30-39", "40-49", "50-100"])
    main("topic_predictions_1.tsv", ['ANIME', 'AUTO-MOTO', 'BIKES', 'CELEBRITIES', 'ENTERTAINMENT', 'MEDICINE-AESTHETICS',
                 'METAL-DETECTING', 'NATURE', 'SMOKE', 'SPORTS', 'TECHNOLOGY'])
    main("gender_predictions_1.tsv", ['M', 'F'])
