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
    # 83.33333333333334
    # 83.33333333333334
    #  100.0

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    print(Border)
    print("Accuracy of the model is :", Accuracy*100)

    print(Border)
    print("If randon_state=0 then accuracy is 83.33333333333334")
    print("If random_state=10 then accuracy is 83.33333333333334")
    print("If random_state=42 then accuracy is 100.0")
    print("random state 0 and 10 gives same model accuracy while 42 gives 100 accuracy.")

    print(Border)

if __name__ == "__main__":
    main()