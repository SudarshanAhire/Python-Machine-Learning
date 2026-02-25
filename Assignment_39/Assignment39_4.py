import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

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

    Accu_Score = accuracy_score(Y_pred, Y_test)
    
    con_matrix = confusion_matrix(Y_test, Y_pred)

    # TP -> True Positive -> if actual value is PASS then it give PASS.
    # TN -> True Negative -> if actual value is FAIL then it give FAIL.
    # FP -> Flase Positive -> if actual value is FAIL then it give PASS.
    # FN -> Flase Negative -> if actual value is PASS then it give FAIL.

    print("-"*100)
    print("Confusion matrix :")
    print(con_matrix)
    print("-"*100)

    data = ConfusionMatrixDisplay(confusion_matrix = con_matrix, display_labels = model.classes_)
    data.plot()

    plt.title("Confusion Matrix")
    plt.show()
    
if __name__ == "__main__":
    main()