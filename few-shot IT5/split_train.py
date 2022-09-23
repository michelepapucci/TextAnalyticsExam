import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv("training_filtered.csv")
    df = df.sample(frac=1).reset_index(drop=True)
    df1 = df.iloc[:2711, :]
    df2 = df.iloc[2711:5421, :]
    df3 = df.iloc[5421:8131, :]
    df4 = df.iloc[8131:10841, :]
    df1.to_csv("training_1_shot.csv")
    df2.to_csv("training_2_shot.csv")
    df3.to_csv("training_3_shot.csv")
    df4.to_csv("training_4_shot.csv")
