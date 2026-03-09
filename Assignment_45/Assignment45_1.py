import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #------------------------------------------------------------------------------------
    # Strp 1 - Load the dataset from csv file
    #------------------------------------------------------------------------------------

    print(Border)
    print("Strp 1 - Load the dataset from csv file")
    print(Border)

    df = pd.read_csv(DataPath)
    print(Border)
    print("Some Entries from dataset")
    print(df.head())
    print(Border)

    #------------------------------------------------------------------------------------
    # Step 2 - Clean the dataset from removing empty rows
    #------------------------------------------------------------------------------------

    print(Border)
    print("Step 2 - Clean the Dataset from removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total records :", df.shape[0])
    print("Total clumns :", df.shape[1])
    print(Border)

    #------------------------------------------------------------------------------------
    # Step 3 - Separeate independeant and dependant variables
    #------------------------------------------------------------------------------------

    print(Border)
    print("Step 3 - Separeate independeant and dependant variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print(Border)
    print("Input columns :", X.columns.tolist())
    print("Output column : Class")

    #------------------------------------------------------------------------------------
    # Step 4 - Split the dataset for training and testing
    #------------------------------------------------------------------------------------

    print(Border)
    print("Step 4 - Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    print(Border)
    print("Information of training and testind data")
    print("X_train shape :", X_train.shape)
    print("X_test shape :", X_test.shape)
    print("Y_train shape :", Y_train.shape)
    print("Y_test shape :", Y_test.shape)

    #------------------------------------------------------------------------------------
    # Step 5 - Feature Scalling
    #------------------------------------------------------------------------------------

    print(Border)
    print("Step 5 - Feature Scalling")
    print(Border)

    scaler = StandardScaler()
    # Independent variables scalling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature Scalling is done")

    #------------------------------------------------------------------------------------
    # Step 6 - Explore the multiple values of K
    # HyperParameter tunning (K)
    #------------------------------------------------------------------------------------

    accuracy_scores = []
    K_values = range(1, 21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy*100)

    print(Border)
    print("Accuracy report of all k values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    #------------------------------------------------------------------------------------
    # Step 7 - Plot graph of k vs accuarcy
    #------------------------------------------------------------------------------------
    print(Border)
    print("Step 7 - Plot graph of k vs accuarcy")
    print(Border)

    plt.figure(figsize=(8, 5))
    plt.plot(K_values, accuracy_scores, marker='o')
    plt.xlabel("K Values")
    plt.ylabel("Accuracy Scores")
    plt.title("K Values vs Accuracy Scores")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

    #------------------------------------------------------------------------------------
    # Step 8 - find best values of k
    #------------------------------------------------------------------------------------
    print(Border)
    print("Step 8 - find best values of k")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of k is :", best_k)

    #------------------------------------------------------------------------------------
    # Step 9 - Build Final model using best value of k 
    #------------------------------------------------------------------------------------
    print(Border)
    print("Step 9 - Build Final model using best value of k") 
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)

    final_model.fit(X_train_scaled, Y_train)

    Y_pred = final_model.predict(X_test_scaled)

    #------------------------------------------------------------------------------------
    # Step 10 - Calculate final accuracy 
    #------------------------------------------------------------------------------------
    print(Border)
    print("Step 10 - Calculate final accuracy") 
    print(Border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of the model is :", accuracy*100)

    #------------------------------------------------------------------------------------
    # Step 11 - Display confusion matrics 
    #------------------------------------------------------------------------------------
    print(Border)
    print("Step 11 - Display confusion matrics") 
    print(Border)

    cm = confusion_matrix(Y_test, Y_pred)

    print(cm)

    #------------------------------------------------------------------------------------
    # Step 12 - Display classification report 
    
    print(Border)
    print("Step 12 - Display classification report") 
    print(Border)

    print(classification_report(Y_test, Y_pred))

    print(Border)


def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()