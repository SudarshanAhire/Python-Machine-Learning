import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    
    #-----------------------------------------------------
    # Step 1 - Exploratory Data Analysis
    #-----------------------------------------------------
    Border = "-"*50

    df = pd.read_csv("diabetes.csv")

    print(Border)
    print("First five records of dataset :")
    print(df.head())
    print(Border)

    print("Missing values of clumns and column information :")
    print(df.isnull().sum())
    print(Border)

if __name__ == "__main__":
    main()