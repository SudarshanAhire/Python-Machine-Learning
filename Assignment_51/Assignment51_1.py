import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import VotingClassifier

def main():
    #------------------------------------------------------
    # Step 1 - Load Dataset and Preprocessing
    #------------------------------------------------------
    Border = "-"*50
    print(Border)
    print("Step 1 - Load Dataset and Preprocessing ")
    print(Border)

    true_data = pd.read_csv("True.csv")

    fake_data = pd.read_csv("Fake.csv")

    print("Dataset entris before adding lables :")
    print(true_data.head())
    print(Border)

    true_data['label'] = 1
    print("Dataset entris after adding lables :")
    print(true_data.head())
    print(Border)

    print("Dataset entris before adding lables :")
    print(fake_data.head())
    print(Border)

    fake_data['label'] = 0
    print("Dataset entris after adding lables :")
    print(fake_data.head())
    print(Border)

    data = [true_data, fake_data]

    df = pd.concat(data)

    print("Dataset after concatinating :")
    print(df.head(10))
    print(Border)

    #------------------------------------------------------
    # Step 2 - Analysis and Preprocessing Of Dataset
    #------------------------------------------------------
    print("Step 2 - Analysis and Preprocessing of Dataset")
    print(Border)

    print("Shape of the dataset :", df.shape)
    print(Border)
    print("Columns in the dataset :", list(df.columns))
    print(Border)

    print("Missing values count in the dataset :")
    print(df.isnull().sum())
    print(Border)

    #------------------------------------------------------
    # Step 3 - Feature Extraction And TF-IDF Vectorization
    #------------------------------------------------------
    print("Step 3 - Feature Extraction and TF_IDF vectorization")
    print(Border)

    X = df['title'] + " " + df['text']
    Y = df['label']

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(X)

    #------------------------------------------------------
    # Step 4 - Model Building
    #------------------------------------------------------
    print("Step 4 - Model Building")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    lr_model = LogisticRegression(max_iter=1000)
    dt_model = DecisionTreeClassifier(random_state=42)

    lr_model.fit(X_train, Y_train)
    dt_model.fit(X_train, Y_train)

    hard_model = VotingClassifier(
        estimators = [
        ('lr', lr_model),
        ('dt', dt_model)
    ],
    voting='hard'
    )

    hard_model.fit(X_train, Y_train)

    Y_pred_hard = hard_model.predict(X_test)


    soft_model = VotingClassifier(
        estimators=[
            ('lr', lr_model),
            ('dt', dt_model)
        ],
        voting='soft'
    )

    soft_model.fit(X_train, Y_train)

    Y_pred_soft = soft_model.predict(X_test)

    #------------------------------------------------------
    # Step 5 - Evaluation of models
    #------------------------------------------------------
    print("Step 5 - Evaluation of models")
    print(Border)

    acc_hard = accuracy_score(Y_test, Y_pred_hard)

    acc_soft = accuracy_score(Y_test, Y_pred_soft)

    print("Accuracy of the hard model :", acc_hard)
    print("Accuracy of the soft model :", acc_soft)
    print(Border)

    cm_hard = confusion_matrix(Y_test, Y_pred_hard)
    print("Confusion matrix of hard model :")
    print(cm_hard)
    print(Border)

    cm_soft = confusion_matrix(Y_test, Y_pred_soft) 
    print("Confusion matrix of soft model :")
    print(cm_soft)
    print(Border)

    print(f"Accuracy of hard voting model : {acc_hard:.4f} vs soft voting model : {acc_soft:.4f}")
    print(Border)


if __name__ == "__main__":
    main()