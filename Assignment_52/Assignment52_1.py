import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.cluster import k_means

def main():
    #----------------------------------------------------------
    # Step 1 - Load the dataset
    #----------------------------------------------------------

    df = pd.read_csv("student-mat.csv")

    print(df.head())
    

if __name__ == "__main__":
    main()
