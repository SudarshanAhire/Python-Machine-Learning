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

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    print(Border)
    print("Accuracy of the model is :", Accuracy*100)

    print(Border)
    print("The new accuracy of the model is same as the previous accuracy of the model.")
    print("As per my observation, removing the feature 'SleepHours' does not Afeest model performance.")

    print(Border)

if __name__ == "__main__":
    main()