import pandas as pd

def main():

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    Border = "-"*50

    print(Border)
    print("Total number of students :", len(df.FinalResult))

    print(Border)
    PassedStudents = 0
    for i in range(len(df.FinalResult)):
        if df.FinalResult[i] == 1:
            PassedStudents = PassedStudents + 1

    print("Total number of passed students :", PassedStudents)

    print(Border)
    FailedStudents = 0
    for i in range(len(df.FinalResult)):
        if df.FinalResult[i] == 0:
            FailedStudents = FailedStudents + 1

    print("Total number of failed students :", FailedStudents)
    
    print(Border)

if __name__ == "__main__":
    main()

