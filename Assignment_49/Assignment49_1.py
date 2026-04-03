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
    print("Step 1 - Exploratory Data Analysis :")

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
    print(Border)

    print("Histogram of the target variable :")
    plt.figure(figsize=(8, 5))
    plt.hist(df['Outcome'], bins=10, color='skyblue', edgecolor='black')
    plt.show()
    print(Border)

    print("Outliers Visualization in the dataset :")
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df)
    plt.title("Boxplot - detection of outliers")
    plt.show()
    print(Border)

    print("Pairplot of the dataset :")
    plt.figure(figsize=(8, 5))
    sns.pairplot(df, hue='Outcome')
    plt.show()
    print(Border)

    #-----------------------------------------------------
    # Step 2 - Data Preprocessing
    #-----------------------------------------------------
    print("Step 2 - Data Preprocessing :")
    print(Border)

    print("Missing values in Glucose :", df["Glucose"].isnull().sum())
    print(Border)
    print("Missing values in bloodpressure :", df["BloodPressure"].isnull().sum())
    print(Border)

    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True)
    plt.show()

    X = df[['Glucose', 'Insulin', 'BMI', 'Age']]
    Y = df['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Dataset after scaling :")
    print(X_scaled[:10])
    print(Border)

    #-----------------------------------------------------
    # Step 3 - Mdodel Building
    #-----------------------------------------------------
    print("Step 3 - Model Building :")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    model_1 = DecisionTreeClassifier(criterion='gini', random_state=42, max_depth=4)

    model_2 = KNeighborsClassifier(n_neighbors=7)

    model_3 = LogisticRegression(max_iter=200)

    model_1.fit(X_train, Y_train)
    model_2.fit(X_train, Y_train)
    model_3.fit(X_train, Y_train)

    Y_pred1 = model_1.predict(X_test)
    Y_pred2 = model_2.predict(X_test)
    Y_pred3 = model_3.predict(X_test)

    #-----------------------------------------------------
    # Step 4 - Model Evaluation
    #-----------------------------------------------------
    print("Step 4 - model Evaluation :")
    print(Border)

    acc1 = accuracy_score(Y_test, Y_pred1)
    print("Accuracy of Decision Tree Classifier :", acc1)
    print(Border)

    acc2 = accuracy_score(Y_test, Y_pred2)
    print("Accuracy of K-Nearest Neighbors Classifier :", acc2)
    print(Border)

    acc3 = accuracy_score(Y_test, Y_pred3)
    print("Accuracy of Logistic Regression Classifier :", acc3)

    print(Border)
    cm1 = confusion_matrix(Y_test, Y_pred1)
    print("Confusion Matrix - Decision Tree:")
    print(cm1)
    print(Border)

    cm2 = confusion_matrix(Y_test, Y_pred2)
    print("Confusion Matrix - K-Nearest Neighbors:")
    print(cm2)
    print(Border)

    cm3 = confusion_matrix(Y_test, Y_pred3)
    print("Confusion Matrix - Logistic Regression:")
    print(cm3)

    print(Border)
    cr1 = classification_report(Y_test, Y_pred1)
    print("Classification Report - Decision Tree:")
    print(cr1)
    print(Border)

    cr2 = classification_report(Y_test, Y_pred2)
    print("Classification Report - K-Nearest Neighbors:")
    print(cr2)
    print(Border)

    cr3 = classification_report(Y_test, Y_pred3)
    print("Classification Report - Logistic Regression:")
    print(cr3)
    print(Border)

    print("Visualization of confusion matrix for Decision Tree Classifier :")
    plt.figure(figsize=(8, 5))
    sns.heatmap(cm1, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Decision Tree")
    plt.show()
    print(Border)

    print("Visualization of confusion matrix for K-Neighbour Classifier :")
    plt.figure(figsize=(8, 5))
    sns.heatmap(cm2, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - K-Neighbour Classifier")
    plt.show()
    print(Border)

    print("Visualization of confusion matrix for Logistic Regression :")
    plt.figure(figsize=(8, 5))
    sns.heatmap(cm3, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Logistic Regression")
    plt.show()
    print(Border)

    #-----------------------------------------------------
    # Step 5 - Final Output
    #-----------------------------------------------------
    print("Step 5 - Final Output :")
    print(Border)

    print("Actual values of target variable :")
    print(Y_test)
    print(Border)

    print("Prediction of the target variable for Decision Tree Classifier :")
    print(Y_pred1)
    print(Border)

    print("Prediction of the target variable for K-Nearest Neighbors Classifier :")
    print(Y_pred2)
    print(Border)

    print("Prediction of the target variable for Logistic Regression Classifier :")
    print(Y_pred3)
    print(Border)
        

    Prediction = pd.DataFrame()

    Prediction[["Y_pred1", "Y_pred2", "Y_pred3"]] = pd.DataFrame({
        "Y_pred1": Y_pred1,
        "Y_pred2": Y_pred2,
        "Y_pred3": Y_pred3
    })

    Prediction["Actual"] = Y_test.reset_index(drop=True)

    Prediction.to_csv("Prediction.csv", index=False)
    print("Predictions.csv created succesully...")
    print(Border)


if __name__ == "__main__":
    main()