import pandas as pd 

def main():

    Dataset = "student_performance_ml.csv"

    df =  pd.read_csv(Dataset)

    Border = "-"*100

    print(Border)
    Pass, Fail = df["FinalResult"].value_counts()
    print("Pass student count :", Pass)
    print("Fail student count :", Fail)

    print(Border)
    Pass_Percentage = (Pass / len(df.FinalResult)) * 100
    print("Passing percentage :", Pass_Percentage)

    print(Border)
    Fail_Percentage = (Fail / len(df.FinalResult)) * 100
    print("Fail Percentage :", Fail_Percentage)

    print(Border)
    print("Yes, the dataset is balanced. It contains a 60/40 split—where \n60% of students passed and 40% failed—which is an acceptable ratio for a balanced dataset.")

    print(Border)

if __name__ == "__main__":
    main()