from sklearn.preprocessing import StandardScaler
import math

def main():
    
    X = [
        [25, 20000],
        [30, 40000],
        [35, 80000]]
    
    EucDistance = math.sqrt(((X[1][0] - X[0][0]) ** 2) + ((X[1][1] - X[1][0]) ** 2))
    print("EUC Distance before scalling :", EucDistance)
    
    scaler = StandardScaler()
        
    X_scaled = scaler.fit_transform(X)

    EucDistance = math.sqrt(((X_scaled[1][0] - X_scaled[0][0]) ** 2) + ((X_scaled[1][1] - X_scaled[1][0]) ** 2))
    print("EUC Distance after scalling :", EucDistance)

    Explanation = """
    Before scalling the second column feature dominates or controls the output
    but, after scalling both the features in the dataset contribute equally.
    """

    print(Explanation)
    

if __name__ == "__main__":
    main()