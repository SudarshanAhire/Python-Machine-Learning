import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    X = [[1], [2], [3], [4], [5]]
    Y = [50, 55, 60, 65, 70]

    model = LinearRegression()

    model.fit(X, Y)

    Y_pred = model.predict(X)

    print("Predicted Data :",)
    print(Y_pred)

    print("Coefficient :", model.coef_)

    print("Intercept :", model.intercept_)

    
if __name__ == "__main__":
    main()