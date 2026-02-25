import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    plt.scatter(df["AssignmentsCompleted"], df["FinalResult"])

    plt.grid(True)
    plt.xlabel("Assignments Completed")
    plt.ylabel("FinalResult")
    plt.title("Relationship between Assignments completed & FinalResult")
    
    plt.show()

    print("-"*100)
    print("Students who have completed five or more assignments pass the exam, while students \nwho have completed fewer than five assignments fail the exam.\n"
      "Conclusion: To pass the exam, students need to complete more than five assignments.")
    print("-"*100)

if __name__ == "__main__":
    main()