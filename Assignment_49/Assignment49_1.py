import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.preprocessing import StandardScaler

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

    print("Column info and missing values :")
    print(df.isnull().sum())
    print(Border)

    print("Statistical inforamtion of dataset :")
    print(df.describe())
    print(Border)

    # print("Plotting of the target variable :")
    # sns.countplot(x='Outcome', data=df)
    # plt.show()

    # print("Plotting with histogram :")
    # plt.figure(figsize=(8, 5))
    # plt.hist(df['Outcome'], bins=10, color='skyblue', edgecolor='black')
    # plt.show()

    # print("Plotting with boxplot :")
    # plt.figure(figsize=(8, 5))
    # sns.boxplot(data=df)
    # plt.title("Boxplot - detection of outliers")
    # plt.show()

    # print("Plotting with pairplot :")
    # plt.figure(figsize=(8, 5))
    # sns.pairplot(df, hue='Outcome')
    # plt.show()

    #-----------------------------------------------------
    # Step 2 - Data Preprocessing
    #-----------------------------------------------------

    print("Missing values in Glucose :", df["Glucose"].isnull().sum())
    print("Missing values in bloodpressure :", df["BloodPressure"].isnull().sum())

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)




if __name__ == "__main__":
    main()