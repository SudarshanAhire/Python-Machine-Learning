import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    plt.figure(figsize=(8, 5))

    sns.boxplot(df["Attendance"], color="skyblue")

    plt.show()

if __name__ == "__main__":
    main()