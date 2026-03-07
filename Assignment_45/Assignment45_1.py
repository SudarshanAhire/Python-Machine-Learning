import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def WinePredictor(FilePath):
    Border = "-"*40

    #--------------------------------------------------------------
    # Step 1 - Laod dataset
    #--------------------------------------------------------------
    print(Border)
    print("Step 1 - Load Dataset")
    print(Border)

    df = pd.read_csv(FilePath)

    print("Few records from file :")
    print(df.head())

    #--------------------------------------------------------------
    # Step 2 - Check missing values
    #--------------------------------------------------------------
    print(Border)
    print("Step 2 - Check missing values")
    print(Border)

    print("Missing count :")
    print(df.isnull().sum())

    #--------------------------------------------------------------
    # Step 3 - Display Statistical summury
    #--------------------------------------------------------------
    print(Border)
    print("Step 3 - Display Statistical summury")
    print(Border)

    print(df.describe())

    #-----------------------------------------------------------------
    # Step 4 - Correlation between columns
    #-----------------------------------------------------------------
    print(Border)
    print("Step 4 - correlation between columns")
    print(Border)

    print("Correlation matrix")
    print(df.corr())

    #-----------------------------------------------------------------
    # Step 5 - Spliting dataset into depedndent and idependent variables
    #-----------------------------------------------------------------
    print(Border)
    print("Step 5 - Spliting dataset into depedndent and idependent variables")
    print(Border)

    X = df[['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']]
    Y = df['Class']

    print("Shape of independent variables :", X.shape)
    print("Shape of dependent variables :", Y.shape)

    #-----------------------------------------------------------------
    # Step 6 - Split the dataset into traing and testing
    #-----------------------------------------------------------------
    print(Border)
    print("Step 6 - Split the dataset into traing and testing")
    print(Border)   

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train shape :", X_train.shape)
    print("X_test shape :", X_test.shape)
    print("Y_train shape :", Y_train.shape)
    print("Y_test shape :", Y_test.shape)


    #-----------------------------------------------------------------
    # Step 7 - Create and train the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 7 - Create and train the model")
    print(Border)   

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, Y_train)

    #-----------------------------------------------------------------
    # Step 8 - Test the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 8 - Test the model")
    print(Border)

    Y_pred = model.predict(X_test)


    #-----------------------------------------------------------------
    # Step 8 - Evaluate the model
    #-----------------------------------------------------------------
    print(Border)
    print("Step 8 - Evaluate the model")
    print(Border)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of the model :", Accuracy*100)


def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()