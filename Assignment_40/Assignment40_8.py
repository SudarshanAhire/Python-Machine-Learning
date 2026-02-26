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

    Accuracy = accuracy_score(Y_test, Y_pred)
    
    plt.figure(figsize=(8, 5))
    plot_tree(
        model,
        feature_names=features,
        class_names=["Fail", "Pass"],
        filled=True
    )
    plt.show()

    print(Border)
    print("the 'StudyHours' feature appears at the root.")
    print("the decision tree chose 'StudyHours' as the most informative feature for the first split.")

    print(Border)

if __name__ == "__main__":
    main()