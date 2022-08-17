import pandas as pd
from libraries.Experiment.training_data_parser import TrainingDataParser
from libraries.Experiment.training_data_filter import TrainingDataFilter


def main(src_path, output_name):
    parser = TrainingDataParser(src_path)
    parser.to_csv(file_output=True, output_name=output_name)

    df = pd.read_csv('src/data/post_processed/' + output_name)
    filter = TrainingDataFilter(df)

    filter.filter_short_sentences(10)
    df = filter.get_data()

    with open(f"src/data/post_processed/filtered.csv", "w") as file_output:
        df.to_csv(file_output, index=False)

    print(df.head(100))


if __name__ == '__main__':
    main('src/data/original/test_task1.txt', 'test_1.csv')
