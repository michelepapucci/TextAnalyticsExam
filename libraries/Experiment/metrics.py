from sklearn.metrics import classification_report, roc_curve, auc, roc_auc_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Metrics:

    def __init__(self, prediction_path, labels=None):
        self.y_proba = None
        self.y_pred = None
        self.y_true = None
        self.predictions_path = prediction_path
        self.labels = labels

        self.extract_predictions()

    def extract_predictions(self):
        df = pd.read_csv(self.predictions_path, sep="\t")
        self.y_true = df['y_true'].values
        self.y_pred = df['y_pred'].values
        # self.y_proba = df['y_proba'].values

    def plot_multiclass_roc(self, output_path="/output/", title='ROC', figsize=(17, 6)):
        # structures
        n_classes = len(list(set(self.y_true)))
        fpr = dict()
        tpr = dict()
        roc_auc = dict()

        # calculate dummies once
        y_test_dummies = pd.get_dummies(self.y_true, drop_first=False).values
        for i in range(n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_test_dummies[:, i], self.y_proba)
            roc_auc[i] = auc(fpr[i], tpr[i])

        # roc for each class
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot([0, 1], [0, 1], 'k--')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title(title, fontsize=30)
        for i in range(n_classes):
            ax.plot(fpr[i], tpr[i], label=f"{self.labels[i]}: AUC {round(roc_auc[i], 4)}")
        ax.legend(loc="best")
        plt.legend(fontsize=15)
        ax.grid(alpha=.4)
        sns.despine()
        plt.savefig(f'{output_path}roc.png', format='png', dpi=70)

    def report(self, output_path=None):
        report = classification_report(self.y_true, self.y_pred) if self.labels is None \
            else classification_report(self.y_true, self.y_pred, labels=[i for i in range(0, len(self.labels))],
                                       target_names=self.labels)
        print(report)
        if output_path is not None:
            with open(f"{output_path}classification_report.txt", "w") as output:
                output.write(report)
        # self.plot_multiclass_roc(output_path)


if __name__ == '__main__':
    m = Metrics("../../output/gender/bert_for_gender_predictions.tsv", ['Male', 'Female'])
    m.report("")
