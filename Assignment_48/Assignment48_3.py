import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    
    X = [
        [25, 20000],
        [30, 40000],
        [35, 80000]]
    
    scaler = StandardScaler()
    
    X_scaled = scaler.fit_transform(X)

    print("Scaled Dataset :")

    print(X_scaled)
    


if __name__ == "__main__":
    main()