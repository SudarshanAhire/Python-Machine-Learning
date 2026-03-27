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

    df = pd.read_csv("student-mat.csv", sep=";")

    print(df.head())

    print(df.shape)
    print(df.isnull().sum())

    X = df[['G1', 'G2', "G3",'studytime', 'absences', 'failures']]

    print(X.head())

    print(X.describe())

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # plt.boxplot(X)
    # plt.show()
    
    model = KMeans(n_clusters=3, random_state=42)

    model.fit(X)

    # cluster = model.fit_predict(X_scaled)

    # df['Cluster'] = cluster

    Y_pred = model.predict([[5, 6, 6, 2, 6, 0]])

    # print(df.head())
    print(Y_pred)


if __name__ == "__main__":
    main()
