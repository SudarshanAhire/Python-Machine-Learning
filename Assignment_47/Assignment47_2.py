import pandas as pd
import numpy as np

def main():
    X = np.array([4, 6, 8, 10, 12])

    # Calculation of mean
    sum = 0
    for val in X:
        sum = sum + val

    mean_X = sum / len(X)
    print("Mean of X is :", mean_X)

    # Calculation of deviation
    deviation = []
    for val in X:
        deviation_of_val = (val - mean_X)
        print(f"Deviation of {val} is :", deviation_of_val)
        deviation.append(float(deviation_of_val))

    # Calculating square of each deviation
    Square_of_deviation = [val*val for val in deviation]
    print("Square of each deviation val :", Square_of_deviation)

    # calculating the varience of dataset
    sum = 0
    for val in Square_of_deviation:
        sum = sum + val

    variance = sum / len(Square_of_deviation)
    print("Variance of the dataset is :", variance)


if __name__ == "__main__":
    main()