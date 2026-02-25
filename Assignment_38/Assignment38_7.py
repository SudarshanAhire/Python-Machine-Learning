import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    for fn in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == fn]
        plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = fn)

    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.title("StudyHours vs PreviousScore")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()