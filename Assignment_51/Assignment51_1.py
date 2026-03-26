import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    #------------------------------------------------------
    # Step 1 - Load Dataset and Preprocessing
    #------------------------------------------------------

    true_data = pd.read_csv("True.csv")

    fake_data = pd.read_csv("Fake.csv")

    print("Dataset entris before adding lables :")
    print(true_data.head())

    true_data['label'] = 1
    print("Dataset entris after adding lables :")
    print(true_data.head())

    print("Dataset entris before adding lables :")
    print(fake_data.head())

    fake_data['label'] = 0
    print("Dataset entris after adding lables :")
    print(fake_data.head())

    data = [true_data, fake_data]

    df = pd.concat(data)

    print("Dataset after concatinating :")
    print(df.head(10))

    #------------------------------------------------------
    # Step 2 - Analysis and Preprocessing Of Dataset
    #------------------------------------------------------

    


if __name__ == "__main__":
    main()