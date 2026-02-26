import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[features]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, Y_train)

    print(Border)
    print("Feature importance :")
    print(model.feature_importances_)

    print(Border)
    print("Feature which contributes more in predicting the result :", "Attendence")

    print(Border)
    print("Feature's which contributes less for predicting the result :", "StudyHours, PreviousScore, AssignmentsCompleted, SleepHours")

    print(Border)

if __name__ == "__main__":
    main()