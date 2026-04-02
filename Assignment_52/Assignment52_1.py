import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler

def main():
    #----------------------------------------------------------
    # Step 1 - Load the dataset
    #----------------------------------------------------------

    print("Step 1 - Load the dataset")
    df = pd.read_csv("student-mat.csv", sep=";")

    print("First few records of dataset :")
    print(df.head())

    print("Shape of the dataset :")
    print(df.shape)

    print("Missing values of dataset :")
    print(df.isnull().sum())

    X = df[['G1', 'G2', "G3",'studytime', 'absences', 'failures']]

    print(X.head())

    print(X.describe())

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print(X_scaled[:5])

    WCSS = []

    for i in range(1, 11):
        model = KMeans(n_clusters=i, random_state=42, n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), WCSS, marker='o')
    plt.grid(True)
    plt.show()
    
    #--------------------------------------------------------
    # Train the model 
    #--------------------------------------------------------

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = model.fit_predict(X_scaled)

    df['cluster'] = clusters 
    print(df.head())    

    labels = model.labels_
    print("Cluster labels : ", labels)

    centriods = model.cluster_centers_
    print("Centriods : ", centriods)


    
if __name__ == "__main__":
    main()
