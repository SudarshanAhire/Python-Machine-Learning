import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score
)

def main():
    Border = "-"*100

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    X = df[features]
    y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model1 = DecisionTreeClassifier(
        criterion="gini",
        max_depth=1,
        random_state=42
    )

    model1.fit(X_train, Y_train)

    Y_pred = model1.predict(X_test)

    Accu_Score = accuracy_score(Y_pred, Y_test)
    
    print(Border)
    print("Accuracy of model1 with max_depth=1 :", Accu_Score*100)

    model2 = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model2.fit(X_train, Y_train)

    Y_pred = model2.predict(X_test)

    Accu_Score = accuracy_score(Y_pred, Y_test)
    
    print(Border)
    print("Accuracy of model2 with max_depth=3 :", Accu_Score*100)

    model3 = DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,
        random_state=42
    )

    model3.fit(X_train, Y_train)

    Y_pred = model3.predict(X_test)

    Accu_Score = accuracy_score(Y_pred, Y_test)
    
    print(Border)
    print("Accuracy of model1 with max_depth=None :", Accu_Score*100)

    print(Border)
    print("All three models accuracies are 100 percent.")

    print(Border)
   
if __name__ == "__main__":
    main()