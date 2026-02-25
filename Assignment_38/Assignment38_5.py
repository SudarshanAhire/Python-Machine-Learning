import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    Border = "-"*100

    plt.scatter(df["StudyHours"], df["FinalResult"])
    plt.xlabel("Study Hours")
    plt.ylabel("Final Result")
    plt.grid(True)
    plt.show()

    print(Border)
    print("Yes, Higher study hours increase the chance of passing.")

    plt.scatter(df["Attendance"], df["FinalResult"])
    plt.xlabel("Attendance")
    plt.ylabel("Final Result")
    plt.grid(True)
    plt.show()

    print(Border)
    print("Yes, with the help of above relationship graph between the attendance and final result.\nwe can say that higher attendace improves final result.")

    print(Border)

if __name__ == "__main__":
    main()