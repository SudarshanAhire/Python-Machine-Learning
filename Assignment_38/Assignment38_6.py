import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    plt.figure(figsize=(8, 5))
    plt.xlabel("Study Hours")
    plt.ylabel("Student Count")
    plt.title("Analysis of study hours")

    sns.histplot(df["StudyHours"])

    plt.show()

    print("-"*110)
    print("According to the histogram graph, we can say that the data is uniformaly distributed accross the  dataset.")
    print("-"*110)


if __name__ == "__main__":
    main()