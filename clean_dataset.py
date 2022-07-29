import pandas as pd
from training_data_parser import TrainingDataParser
from training_data_filter import TrainingDataFilter


def main():
    src_path = 'src/data/original/training.txt'
    parser = TrainingDataParser(src_path)
    parser.to_csv(file_output=True)

    df = pd.read_csv('src/data/post_processed/training.csv')
    filter = TrainingDataFilter(df)

    filter.filter_short_sentences(10)
    df = filter.get_data()

    with open("src/data/post_processed/training_filtered.csv", "w") as file_output:
        df.to_csv(file_output, index=False)

    print(df.head(100))


if __name__ == '__main__':
    main()
