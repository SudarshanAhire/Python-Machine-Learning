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

    New_df = pd.read_csv("New_Student_Data.csv")

    Y_pred = model.predict(New_df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]])

    print(Border)
    print("New Student data's predicted values :", Y_pred)

    print(Border)
    print("New student data's actual values :")
    print(New_df["FinalResult"])

    print(Border)

if __name__ == "__main__":
    main()