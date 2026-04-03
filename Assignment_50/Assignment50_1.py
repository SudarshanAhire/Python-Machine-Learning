import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report, 
    roc_auc_score, 
    RocCurveDisplay, 
    ConfusionMatrixDisplay
)

def main():

    #------------------------------------------------------------
    # Step 1 - Load the dataset
    #------------------------------------------------------------
    Border = "*"*50
    print(Border)
    print("Step 1 - Load the Dataset")
    print(Border)

    df = pd.read_csv("bank-full.csv", sep=";")

    #------------------------------------------------------------
    # Step 2 - Analysis of the dataset
    #------------------------------------------------------------
    print("Step 2 - Analysis of the dataset")
    print(Border)

    print("Shape of dataset :", df.shape)
    print(Border)
    
    print("First few records of dataset :")
    print(df.head())
    print(Border)

    print("Columns in dataset :")
    print(list(df.columns))
    print(Border)

    print("Statistical information of dataset :")
    print(df.describe())
    print(Border)

    print("Missing values of dataset :")
    print(df.isnull().sum())
    print(Border)

    #------------------------------------------------------------
    # Step 3 - Visualization of dataset
    #------------------------------------------------------------
    print("Step 3 - Visualization of dataset ")
    print(Border)

    sns.countplot(x='y', data=df)
    plt.title("Target Variable Distribution")
    plt.show()

    plt.figure(figsize=(10,6))
    sns.boxplot(data=df[['age','balance','duration']])
    plt.title("Boxplot for Outliers")
    plt.show()

    sns.countplot(x='job', hue='y', data=df)
    plt.xticks(rotation=45)
    plt.title("Job vs Target")
    plt.show()

    sns.pairplot(df[['age','balance','duration','y']], hue='y')
    plt.show()

    #------------------------------------------------------------
    # Step 4 - preprocessing and feature encoding
    #------------------------------------------------------------
    print("Step 4 - Preparation and feature encoding")
    print(Border)

    print("Data before preprocessing :")
    print(Border)

    if 'job' in df.columns:
        print("Job column before preprocessing :")
        print(df['job'].head(10))

        df = pd.get_dummies(df, columns=['job'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'marital' in df.columns:
        print("marital column before preprocessing :")
        print(df['marital'].head(10))

        df = pd.get_dummies(df, columns=['marital'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)


    if 'education' in df.columns:
        print("education column before preprocessing :")
        print(df['education'].head(10))

        df = pd.get_dummies(df, columns=['education'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'default' in df.columns:
        print("default column before preprocessing :")
        print(df['default'].head(10))

        df = pd.get_dummies(df, columns=['default'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'housing' in df.columns:
        print("housing column before preprocessing :")
        print(df['housing'].head(10))

        df = pd.get_dummies(df, columns=['housing'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'loan' in df.columns:
        print("loan column before preprocessing :")
        print(df['loan'].head(10))

        df = pd.get_dummies(df, columns=['loan'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'contact' in df.columns:
        print("contact column before preprocessing :")
        print(df['contact'].head(10))

        df = pd.get_dummies(df, columns=['contact'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'month' in df.columns:
        print("month column before preprocessing :")
        print(df['month'].head(10))

        df = pd.get_dummies(df, columns=['month'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'poutcome' in df.columns:
        print("poutcome column before preprocessing :")
        print(df['poutcome'].head(10))

        df = pd.get_dummies(df, columns=['poutcome'], drop_first=True)

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print(Border)

    if 'y' in df.columns:
        print("y column before preprocessing :")
        print(df['y'].head(10))

        df['y'] = df['y'].astype('category').cat.codes
        print("y column after encoding :")
        print(df['y'].head(10))
        print(Border)

    print("Data after preprocessing :")
    print(df.head(10))
    print(Border)


    #------------------------------------------------------------
    # Step 5 - Split the dataset into features and target variable
    #------------------------------------------------------------
    print("Step 5 - Split the dataset into features and target variables")
    print(Border)

    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), annot=False, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

    X = df.drop('y', axis=1)
    Y = df['y']

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("Data after standerd Scalling :")
    print(X_scaled[:10])
    print(Border)

    #------------------------------------------------------------
    # Step 6 - splitting the dataset for train test split
    #------------------------------------------------------------
    print("Step 6 - Splitting the dataset for train test split")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    #------------------------------------------------------------
    # Step 7 - Training classification models
    #------------------------------------------------------------
    print("Training classification models")
    print(Border)

    model_knn = KNeighborsClassifier(n_neighbors=5)  
    model_lr = LogisticRegression(max_iter=1000) 
    model_rf = RandomForestClassifier() 

    model_knn.fit(X_train, Y_train)
    model_lr.fit(X_train, Y_train)
    model_rf.fit(X_train, Y_train)

    Y_pred_knn = model_knn.predict(X_test)
    Y_pred_lr = model_lr.predict(X_test)
    Y_pred_rf = model_rf.predict(X_test)

    #------------------------------------------------------------
    # Step 8 - Evaluation of the model
    #------------------------------------------------------------
    print("Step 8 - Evaluation of the model")
    print(Border)

    knn_acc = accuracy_score(Y_test, Y_pred_knn)
    lr_acc = accuracy_score(Y_test, Y_pred_lr)
    rf_acc = accuracy_score(Y_test, Y_pred_rf)

    print("Accuracy of using KNN :", knn_acc)
    print("Accuracy of using Logistic Regression :", lr_acc)
    print("Accuracy of using Random forest :", rf_acc)
    print(Border)


    print("Confusion Matrix of KNN :")
    knn_cm = confusion_matrix(Y_test, Y_pred_knn)
    print(knn_cm)
    print(Border)

    print("Confusion Matrix of Logistic Regression :")
    lr_cm = confusion_matrix(Y_test, Y_pred_lr)
    print(knn_cm)
    print(Border)

    print("Confusion Matrix of Random forest :")
    rf_cm = confusion_matrix(Y_test, Y_pred_rf)
    print(rf_cm)
    print(Border)

    print("Classification report of knn :")
    knn_cr = classification_report(Y_test, Y_pred_knn)
    print(knn_cr)
    print(Border)

    print("Classification report of Logistic Regression :")
    lr_cr = classification_report(Y_test, Y_pred_lr)
    print(lr_cr)
    print(Border)
    
    print("Classification report of Random Forest :")
    rf_cr = classification_report(Y_test, Y_pred_rf)
    print(rf_cr)
    print(Border)


    print("ROC_AUC Score of KNN :", roc_auc_score(Y_test, Y_pred_knn))
    print("ROC_AUC Score of Logistic Regression :", roc_auc_score(Y_test, Y_pred_lr))
    print("ROC_AUC Score of Random Forest :", roc_auc_score(Y_test, Y_pred_rf))
    print(Border)
    
    #------------------------------------------------------------
    # Step 9 - Plotting confusion matrix and ROC curve
    #------------------------------------------------------------
    print("Step 9 - Plotting confusion matrix and ROC curve")
    print(Border)

    print("Displaying confusion matrix of KNN :")
    disp = ConfusionMatrixDisplay(confusion_matrix=knn_cm, display_labels=model_knn.classes_)
    disp.plot()
    plt.show()
    print(Border)

    print("Displaying confusion matrix of Logistic Regression :")
    disp = ConfusionMatrixDisplay(confusion_matrix=lr_cm, display_labels=model_lr.classes_)
    disp.plot()
    plt.show()
    print(Border)

    print("Displaying confusion matrix of Random Forest :")
    disp = ConfusionMatrixDisplay(confusion_matrix=rf_cm, display_labels=model_rf.classes_)
    disp.plot()
    plt.show()
    print(Border)
    

if __name__ == "__main__":
    main() 