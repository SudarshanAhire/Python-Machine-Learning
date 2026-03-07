from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

def main():

    X = [[1], [2], [3], [4], [5]]
    Y = [20000, 25000, 30000, 35000, 40000]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    Y_Pred = model.predict([[6]])

    print(f"Predicted Salary for 6 Years Experience : ₹{Y_Pred[0]}")

    n = len(X)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    C = mean_y - (m * mean_x)

    x = np.linspace(1, 6, n)
    y = C + m * x

    plt.plot(x, y, color = "g", label = "Regression Line")

    plt.scatter(X, Y, color = 'r', label = "SCatter Plot")

    plt.xlabel("X : Independent Variables")
    plt.ylabel("Y : Dependent Variables")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()