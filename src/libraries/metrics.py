from sklearn.metrics import classification_report
import pandas as pd


class Metrics:

    def __init__(self, prediction_path, labels=None):
        self.y_pred = None
        self.y_true = None
        self.predictions_path = prediction_path
        self.labels = labels

        self.extract_predictions()

    def extract_predictions(self):
        df = pd.read_csv(self.predictions_path, sep="\t")
        self.y_true = df['y_true'].values
        self.y_pred = df['y_pred'].values

    def report(self, output_path=None):
        report = classification_report(self.y_true, self.y_pred) if self.labels is None \
            else classification_report(self.y_true, self.y_pred, labels=[i for i in range(0, len(self.labels))],
                                       target_names=self.labels)
        print(report)
        if output_path is not None:
            with open(f"{output_path}classification_report.txt", "w") as output:
                output.write(report)


if __name__ == '__main__':
    m = Metrics("../../output/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("")
