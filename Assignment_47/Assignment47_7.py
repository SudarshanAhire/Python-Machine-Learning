import numpy as np
from sklearn.preprocessing import StandardScaler

def ScaledVal(val):
    # Givan
    mean_X = 9
    standerd_deviation = 2

    return (val - mean_X) / standerd_deviation

def main():
    X = np.array([6, 7, 8, 9, 10, 11, 12])

    arr = [6, 9, 12]

    for val in arr:
        Scaled_Val = ScaledVal(val)
        print(f"Scaled val for {val} is ", Scaled_Val)

if __name__ == "__main__":
    main()