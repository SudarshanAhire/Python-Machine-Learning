import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("bank-full.csv", sep=";")
    data.to_csv("converted.csv", index=False)

    df = pd.read_csv("converted.csv")

    print(df.head())
    print(df.shape)

    print("MIssing values count :", df.isnull().sum())
    

if __name__ == "__main__":
    main()