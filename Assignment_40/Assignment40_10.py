import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score
)
from sklearn.tree import plot_tree

def main():
    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    df["PerformanceIndex"] = df["StudyHours"] * 2 + df["Attendance"]

    df.drop(columns=["SleepHours"], inplace=True)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "PerformanceIndex"]

    X = df[features]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_train_pred = model.predict(X_train)

    train_accuracy = accuracy_score(Y_train, Y_train_pred)
    
    print(Border)
    print("Training accuracy is :", train_accuracy*100)

    print(Border)
    
    Y_test_pred = model.predict(X_test)

    test_accuracy = accuracy_score(Y_test, Y_test_pred)

    print("Testing accuracy is :", test_accuracy*100)

    print(Border)
    print("Because the decision tree grows until all leaves \nare pure, allowing it to memorize the training data. If the dataset \nis small or perfectly separable, testing accuracy may also be 100%. \nHowever, this may indicate overfitting and poor \ngeneralization to new unseen data.")

    print(Border)
    
if __name__ == "__main__":
    main()