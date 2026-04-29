import numpy as np
import math

def MSE(actual, predicted):
    n = len(actual)
    total_error = 0

    for i in range(n):
        error = actual[i] - predicted[i]
        total_error = total_error + error**2

    mse = total_error / n
    return mse

def Binary_cross_Entropy(actual, predicted):
    n = len(actual)
    total_loss = 0

    for i in range(n):
        y = actual[i]
        p = predicted[i]

        p = max(min(p, 0.999), 0.001)

        loss = -(y * math.log(p) - (1 - y) * math.log(1 - p))
        total_loss = total_loss + loss 

    return total_loss / n

def main():
    
    actual = [1, 0, 1, 1]

    predicted = [0.9, 0.2, 0.8, 0.7]

    mse = MSE(actual, predicted)
    print("Mean Squared Error :", mse)

    bce = Binary_cross_Entropy(actual, predicted)
    print("Binary Cross Entropy Error :", bce)

    print("For Regression we used Mean_sqaured_Error. and \n"
    "For the binary classification we used Binary_Cross_Entropy.")

if __name__ == "__main__":
    main()