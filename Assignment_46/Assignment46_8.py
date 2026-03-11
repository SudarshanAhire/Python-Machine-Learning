from sklearn.linear_model import LinearRegression

def main():
    
    X = [[1], [2], [3], [4], [5]]
    Y = [50, 55, 60, 65, 70]

    model = LinearRegression()

    model.fit(X, Y)

    Y_pred = model.predict([[6]])

    print("Predicted Marks for 6 hours study :", Y_pred[0])

if __name__ == "__main__":
    main()