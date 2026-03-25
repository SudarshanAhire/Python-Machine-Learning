import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    df = pd.read_csv("bank-full.csv", sep=";")

    #------------------------------------------------------------
    # Step 2 - Analysis of the dataset
    #------------------------------------------------------------

    print("Shape of dataset :", df.shape)
    print("First few records of dataset :", df.head())
    print("Columns in dataset :", list(df.columns))

    print("Statistical information of dataset :")
    print(df.describe())

    print("Missing values of dataset :")
    print(df.isnull().sum())


    #------------------------------------------------------------
    # Step 3 - Visualization of dataset
    #------------------------------------------------------------



    #------------------------------------------------------------
    # Step 4 - preprocessing and feature encoding
    #------------------------------------------------------------

    print("Data before preprocessing :")

    if 'job' in df.columns:
        print("Job column before preprocessing :")
        print(df['job'].head(10))

        df['job'] = df['job'].astype('category').cat.codes

        print("job column after encoding :")
        print(df['job'].head(10))

    if 'marital' in df.columns:
        print("marital column before preprocessing :")
        print(df['marital'].head(10))

        df['marital'] = df['marital'].astype('category').cat.codes

        print("marital column after encoding :")
        print(df['marital'].head(10))


    if 'education' in df.columns:
        print("education column before preprocessing :")
        print(df['education'].head(10))

        df['education'] = df['education'].astype('category').cat.codes
        print("education column after encoding :")
        print(df['education'].head(10))

    if 'default' in df.columns:
        print("default column before preprocessing :")
        print(df['default'].head(10))

        df['default'] = df['default'].astype('category').cat.codes
        print("default column after encoding :")
        print(df['default'].head(10))

    if 'housing' in df.columns:
        print("housing column before preprocessing :")
        print(df['housing'].head(10))

        df['housing'] = df['housing'].astype('category').cat.codes
        print("housing column after encoding :")
        print(df['housing'].head(10))

    if 'loan' in df.columns:
        print("loan column before preprocessing :")
        print(df['loan'].head(10))

        df['loan'] = df['loan'].astype('category').cat.codes
        print("loan column after encoding :")
        print(df['loan'].head(10))

    if 'contact' in df.columns:
        print("contact column before preprocessing :")
        print(df['contact'].head(10))

        df['contact'] = df['contact'].astype('category').cat.codes
        print("contact column after encoding :")
        print(df['contact'].head(10))

    if 'month' in df.columns:
        print("month column before preprocessing :")
        print(df['month'].head(10))

        df['month'] = df['month'].astype('category').cat.codes
        print("month column after encoding :")
        print(df['month'].head(10))

    if 'poutcome' in df.columns:
        print("poutcome column before preprocessing :")
        print(df['poutcome'].head(10))

        df['poutcome'] = df['poutcome'].astype('category').cat.codes
        print("poutcome column after encoding :")
        print(df['poutcome'].head(10))

    if 'y' in df.columns:
        print("y column before preprocessing :")
        print(df['y'].head(10))

        df['y'] = df['y'].astype('category').cat.codes
        print("y column after encoding :")
        print(df['y'].head(10))

    print("Data after preprocessing :")
    print(df.head(10))


    #------------------------------------------------------------
    # Step 5 - Split the dataset into features and target variable
    #------------------------------------------------------------

    X = df.drop('y', axis=1)
    Y = df['y']

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("Data after standerd Scalling :")
    print(X_scaled[:10])

    #------------------------------------------------------------
    # Step 6 - splitting the dataset for train test split
    #------------------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    #------------------------------------------------------------
    # Step 7 - Training classification models
    #------------------------------------------------------------

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

    knn_acc = accuracy_score(Y_test, Y_pred_knn)
    lr_acc = accuracy_score(Y_test, Y_pred_lr)
    rf_acc = accuracy_score(Y_test, Y_pred_rf)

    print("Accuracy of using KNN :", knn_acc)
    print("Accuracy of using Logistic Regression :", lr_acc)
    print("Accuracy of using Random forest :", rf_acc)


    print("Confusion Matrix of KNN :")
    knn_cm = confusion_matrix(Y_pred_knn, Y_test)
    print(knn_cm)

    print("Confusion Matrix of Logistic Regression :")
    lr_cm = confusion_matrix(Y_pred_lr, Y_test)
    print(knn_cm)

    print("Confusion Matrix of Random forest :")
    rf_cm = confusion_matrix(Y_pred_rf, Y_test)
    print(rf_cm)

    print("Classification report of knn :")
    knn_cr = classification_report(Y_pred_knn, Y_test)
    print(knn_cr)

    print("Classification report of Logistic Regression :")
    lr_cr = classification_report(Y_pred_lr, Y_test)
    print(lr_cr)
    
    print("Classification report of Random Forest :")
    rf_cr = classification_report(Y_pred_rf, Y_test)
    print(rf_cr)


    print("ROC_AUC Score of KNN :", roc_auc_score(Y_pred_knn, Y_test))
    print("ROC_AUC Score of Logistic Regression :", roc_auc_score(Y_pred_lr, Y_test))
    print("ROC_AUC Score of Random Forest :", roc_auc_score(Y_pred_rf, Y_test))
    
    #------------------------------------------------------------
    # Step 9 - Plotting confusion matrix and ROC curve
    #------------------------------------------------------------

    print("Displaying confusion matrix of KNN :")
    disp = ConfusionMatrixDisplay(confusion_matrix=knn_cm, display_labels=model_knn.classes_)
    disp.plot()
    plt.show()

    print("Displaying confusion matrix of Logistic Regression :")
    disp = ConfusionMatrixDisplay(confusion_matrix=lr_cm, display_labels=model_lr.classes_)
    disp.plot()
    plt.show()

    print("Displaying confusion matrix of Random Forest :")
    disp = ConfusionMatrixDisplay(confusion_matrix=rf_cm, display_labels=model_rf.classes_)
    disp.plot()
    plt.show()
    
    print()

if __name__ == "__main__":
    main() 