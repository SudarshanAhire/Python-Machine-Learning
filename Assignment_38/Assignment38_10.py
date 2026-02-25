import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    plt.scatter(df["SleepHours"], df["FinalResult"])
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")
    plt.title("Relationship between Sleep Hours & Final Result")
    plt.grid(True)

    plt.show()

    print("-"*100)
    print("Yes, sleeping more guarantees success because, as per the \n"\
    "relationship graph, we can see that students who take more sleep pass \n"\
    "the exam, and students who take less sleep fail the exam.")
    print("-"*100)

if __name__ == "__main__":
    main()