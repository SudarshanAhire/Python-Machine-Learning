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
    print("mean of X :", mean_x)

    print(Border)
    mean_y = mean(Y)
    print("mean of Y :", mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print(Border)
    print("Slope (m) :", m)

    C = mean_y - (m * mean_x)

    print(Border)
    print("Y - intercept (C) :", C)

    print(Border)
    print("Regression equation :",)
    print(f"Y = {m}X + {C}")

    print(Border)
    Y_pred = m*6 + C
    print("Predicted Y for X = 6 :", Y_pred)

if __name__ == "__main__":
    main()