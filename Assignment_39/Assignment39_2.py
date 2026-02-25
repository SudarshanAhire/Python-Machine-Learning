import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split


def main():
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[features]
    y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("-"*100)
    print("Predicted Values :",Y_pred)

    print("-"*100)
    print("Actual Values :")
    print(Y_test)
    print("-"*100)

    
if __name__ == "__main__":
    main()