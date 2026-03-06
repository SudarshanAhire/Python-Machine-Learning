import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    Border = "-"*50

    ##########################################################
    # Step 1 - Get Data
    ##########################################################
    
    df = pd.read_csv("Advertising.csv")

    ###########################################################
    # Step 2 - Cleaning, preparation and Manipulation of Data
    ###########################################################

    print(Border)
    print("First five records in dataset :")
    print(df.head())
    print(Border)

    print("Shape of the dataset :", df.shape)
    print(Border)

    print("Column Names :", list(df.columns))
    print(Border)

    print("Statistical Report of Dataset :")
    print(df.describe())

    print(Border)
    print("Count of null values of columns :")
    print(df.isnull().sum())

    df=df.mask(df==0).fillna(df.mean())

    df.drop("Unnamed: 0", axis=1, inplace=True)

    ###########################################################
    # Step 3 - Training Data
    ###########################################################

    X = df[['TV', 'radio', 'newspaper']]
    Y = df[['sales']]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    model = LinearRegression()

    model.fit(X_train, Y_train)

     ###########################################################
    # Step 3 - Testing Data
    ###########################################################

    Y_pred = model.predict(X_test)

    print(Border)
    print("Predicted values of sales :")
    print(Y_pred)
    print(Border)
    print("Actual values of sales :")
    print(Y_test)


if __name__ == "__main__":
    main()