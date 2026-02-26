import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score
)

def main():
    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df =pd.read_csv(Dataset)

    df.drop(columns=["SleepHours"], inplace=True)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]

    X = df[features]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    model1 = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=0
    )

    model1.fit(X_train, Y_train)

    Y_pred = model1.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    print(Border)
    print("Accuracy of model1 with random_state=0 :", Accuracy*100)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

    model2 = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=10
    )

    model2.fit(X_train, Y_train)

    Y_pred = model2.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    print(Border)
    print("Accuracy of model2 with random_state=10 :", Accuracy*100)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model3 = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model3.fit(X_train, Y_train)

    Y_pred = model3.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    print(Border)
    print("Accuracy of model3 with random_state=42 :", Accuracy*100)

    print(Border)
    print("random state 0 and 10 gives same model accuracy while 42 gives 100 accuracy.")

    print(Border)

if __name__ == "__main__":
    main()