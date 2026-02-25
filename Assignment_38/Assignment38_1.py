import pandas as pd 

def main():

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    Border = "-"*100

    print(Border)
    print("First 5 records :")
    print(df.head())

    print(Border)
    print("Last 5 records :")
    print(df.tail())

    print(Border)
    print("Total number of rows and columns :")
    print(df.shape)

    print(Border)
    print("List of column names :")
    print(list(df.columns))

    print(Border)
    print("Datatype of each column :")
    print(df.dtypes)

    print(Border)

if __name__ == "__main__":
    main()