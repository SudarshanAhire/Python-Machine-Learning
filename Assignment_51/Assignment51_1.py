import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    true_data = pd.read_csv("True.csv")

    fake_data = pd.read_csv("Fake.csv")

    true_data['label'] = 1

    fake_data['label'] = 0

    print(true_data.head(10))
    print(fake_data.head(10))

if __name__ == "__main__":
    main()