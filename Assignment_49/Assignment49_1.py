import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
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

    print("Distribution of the target variable :")
    sns.countplot(x='Outcome', data=df)
    plt.show()

    print("Histogram of the target variable :")
    plt.figure(figsize=(8, 5))
    plt.hist(df['Outcome'], bins=10, color='skyblue', edgecolor='black')
    plt.show()

    print("Outliers Visualization in the dataset :")
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df)
    plt.title("Boxplot - detection of outliers")
    plt.show()

    print("Pairplot of the dataset :")
    plt.figure(figsize=(8, 5))
    sns.pairplot(df, hue='Outcome')
    plt.show()

    #-----------------------------------------------------
    # Step 2 - Data Preprocessing
    #-----------------------------------------------------

    print("Missing values in Glucose :", df["Glucose"].isnull().sum())
    print("Missing values in bloodpressure :", df["BloodPressure"].isnull().sum())

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)


    #-----------------------------------------------------
    # Step 3 - Mdodel Building
    #-----------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    model_1 = DecisionTreeClassifier(criterion='gini', random_state=42, max_depth=5)

    model_2 = KNeighborsClassifier(n_neighbors=3)

    model_3 = LogisticRegression()

    model_1.fit(X_train, Y_train)
    model_2.fit(X_train, Y_train)
    model_3.fit(X_train, Y_train)

    Y_pred1 = model_1.predict(X_test)
    Y_pred2 = model_2.predict(X_test)
    Y_pred3 = model_3.predict(X_test)

    #-----------------------------------------------------
    # Step 4 - Model Evaluation
    #-----------------------------------------------------

    acc1 = accuracy_score(Y_test, Y_pred1)
    print("Accuracy of Decision Tree Classifier :", acc1)
    acc2 = accuracy_score(Y_test, Y_pred2)
    print("Accuracy of K-Nearest Neighbors Classifier :", acc2)
    acc3 = accuracy_score(Y_test, Y_pred3)
    print("Accuracy of Logistic Regression Classifier :", acc3)

    print(Border)
    cm1 = confusion_matrix(Y_test, Y_pred1)
    print("Confusion Matrix - Decision Tree:")
    print(cm1)
    cm2 = confusion_matrix(Y_test, Y_pred2)
    print("Confusion Matrix - K-Nearest Neighbors:")
    print(cm2)
    cm3 = confusion_matrix(Y_test, Y_pred3)
    print("Confusion Matrix - Logistic Regression:")
    print(cm3)

    print(Border)
    cr1 = classification_report(Y_test, Y_pred1)
    print("Classification Report - Decision Tree:")
    print(cr1)
    cr2 = classification_report(Y_test, Y_pred2)
    print("Classification Report - K-Nearest Neighbors:")
    print(cr2)
    cr3 = classification_report(Y_test, Y_pred3)
    print("Classification Report - Logistic Regression:")
    print(cr3)

    print("Visualization of cinfusion matrix for Decision Tree Classifier :")
    plt.figure(figsize=(8, 5))
    conf = plot(confusion_matrix=cm1, )

    # print(Border)
    # print(Y_pred1)
    # print(Y_pred2)
    # print(Y_pred3)


if __name__ == "__main__":
    main()