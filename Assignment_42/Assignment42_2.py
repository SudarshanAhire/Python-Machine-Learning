def mean(val):
    sum = 0
    n = len(val) 

    for i in val:
        sum = sum + i

    return sum / n

def main():
    Border = "-"*40
    print(Border)

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    mean_x = mean(X)

    mean_y = mean(Y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    C = mean_y - (m * mean_x)

    print("Predicted Y value for X :")
    for i in X:
        print(f"predicted Y for X = {i} :", m*i + C)

    print(Border)

    Sq_Error_Sum = 0
    for i in range(n):
        Y_Predicted = m * X[i] + C
        Sq_Error_Sum = Sq_Error_Sum + ((Y[i] - Y_Predicted) ** 2)

    MSE = Sq_Error_Sum / n

    print("Mean Square Error (MSE) :", MSE)

    print(Border)

    SS_res = 0
    SS_tot = 0
    
    for i in range(n):
        Y_Predicted = (m * X[i] + C)
        SS_res = SS_res + (Y[i] - Y_Predicted) ** 2
        SS_tot = SS_tot + (Y[i] - mean_y) ** 2

    R_Square = 1- (SS_res / SS_tot)

    print("R_Square Score :", R_Square)

    print(Border)

if __name__ == "__main__":
    main()