import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import BaggingClassifier

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

    print("Shape of the dataset :", df.shape)
    print("Columns in the dataset :", list(df.columns))

    print("Missing values count in the dataset :")
    print(df.isnull().sum())

    #------------------------------------------------------
    # Step 3 - Feature Extraction And TF-IDF Vectorization
    #------------------------------------------------------

    X = df['title'] + " " + df['text']
    Y = df['label']

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(X)

    #------------------------------------------------------
    # Step 4 - Model Building
    #------------------------------------------------------

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    lr_model = LogisticRegression(max_iter=1000)
    dt_model = DecisionTreeClassifier(random_state=42)

    lr_model.fit(X_train, Y_train)
    dt_model.fit(X_train, Y_train)

    hard_model = BaggingClassifier(
        estimator = [
        ('lr', lr_model),
        ('dt', dt_model)
    ],
    voting = 'hard'
    )

    hard_model.fit(X_train, Y_train)

    Y_pred = hard_model.predict(X_test)

    acc = accuracy_score(Y_test, Y_pred)

    print(acc)


if __name__ == "__main__":
    main()