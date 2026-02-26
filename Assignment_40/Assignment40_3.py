import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

def main():
    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance"]

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
    print("Accuracy of the model :", Accuracy*100)

    print(Border)
    cm = confusion_matrix(Y_pred, Y_test)
    print("Confusion matrix :")
    print(cm)

    print(Border)
    print("After comparing the accuracy of this model with full-feature model, \ni conclude that the model is still performing well.")

    print(Border)

if __name__ == "__main__":
    main()