import pandas as pd

def main():

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    Border = "-"*100

    print(Border)
    print("Average of study hours :", df["StudyHours"].mean())

    print(Border)
    print("Average of attendance :", df["Attendance"].mean())

    print(Border)
    print("Maximum previous score :", df["PreviousScore"].max())

    print(Border)
    print("Minimum sleep hours :", df["SleepHours"].min())

    print(Border)

if __name__ == "__main__":
    main()