import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
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

    Ac = accuracy_score(Y_pred, Y_test)

    print(Border)
    print("Accuracy Score :", Ac*100)

    cm = confusion_matrix(Y_pred, Y_test)

    print(Border)
    print("Confusion matrix :")
    print(cm)

    # Confusion matrix :
    # [[5 0]    -> TP = 5, FP = 0
    #  [0 1]]   -> FN = 0, TN = 1

    # Accuracy_matrix = ((TP + TN) / (TP + TN + FP + FN)) * 100

    Manual_accu_calculation = ((5 + 1) / (5 + 1 + 0 + 0)) * 100

    print(Border)
    print("Manual calculation of accutacy :", Manual_accu_calculation)

    print(Border)

if __name__ == "__main__":
    main()