from sklearn.linear_model import LinearRegression

def main():

    X = [[1, 7], [2, 6], [3, 7], [4, 6], [5, 8]]
    Y = [50, 55, 60, 65, 70]

    model = LinearRegression()

    model.fit(X, Y)

    print("Coefficint for StudyHours :", model.coef_[0])
    print("Coefficint for SleepHours :", model.coef_[1])

    print("Value of intercept :", model.intercept_)

if __name__ == "__main__":
    main()