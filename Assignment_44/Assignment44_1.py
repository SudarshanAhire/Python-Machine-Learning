import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score

def main():
    Border = "-"*50
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    print("Shape of dataset :", df.shape)

    print("First five records in Dataset :")
    print(df.head())
    print(Border)

    print("Analysis of dataset :", df.describe())
    print(Border)

    print("Null value count (per column)")
    print(df.isnull().sum())
    print(Border)

    # Alcohol,Malic acid,Ash,Alcalinity of ash,Magnesium,Total phenols,Flavanoids,Nonflavanoid phenols,Proanthocyanins,Color intensity,Hue,OD280/OD315 of diluted wines,Proline

    X = df[['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']]

    Y = df[['Class']]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Predicted Class :")
    print(Y_pred)
    print(Border)

    print("Actual Class are :")
    print(Y_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of the model :", Accuracy*100)


if __name__ == "__main__":
    main()