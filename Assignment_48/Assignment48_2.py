import numpy as np
import math

def main():
    X = [6, 7, 8, 9, 10, 11, 12]

    mean_x = np.mean(X)

    numerator = 0
    denominator = len(X)

    for x in X:
        numerator = numerator + ((x - mean_x) ** 2)

    variance = numerator / denominator

    print("Value of Variance :", variance)

    std = math.sqrt(variance)

    print("Value of standerd deviation :", std)


if __name__ == "__main__":
    main()