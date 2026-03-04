import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def main():
    
    Dataset = [
        {'Study Hours' : 2, 'Attendance' : 60, 'Result' : 'Fail'},
        {'Study Hours' : 5, 'Attendance' : 80, 'Result' : 'Pass'},
        {'Study Hours' : 6, 'Attendance' : 85, 'Result' : 'Pass'},
        {'Study Hours' : 1, 'Attendance' : 50, 'Result' : 'Fail'}
    ]

    Study_Hours = int(input("Enter study hours : "))
    Attendance_percentage = int(input("Enter Attendance : "))

    new_record = {'Study Hours' : Study_Hours, 'Attendance' : Attendance_percentage}

    df = pd.read_csv(Dataset)
    X = df['Study Hours', "Attendance"]
    Y = df['Result']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=2)

    model.fit(X_train, Y_train)

    Y_pred = model.predict()

    print(Y_pred)

if __name__ == "__main__":
    main()