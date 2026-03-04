import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1["X"] - P2["X"]) ** 2 + (P1["Y"] - P2["Y"]) ** 2)
    return Ans

def KNeighborsClassifier():
    Border = "-"*40

    Dataset = [
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
        {"point" : "D", "X" : 4, "Y" : 5, "label" : "Blue"}
    ]

    x_point = int(input("Enter X coordinate : "))
    y_point = int(input("Enter Y coordinate : "))

    new_point = {"X" : x_point, "Y" : y_point}

    for d in Dataset:
        d["distance"] = EucDistance(d, new_point)

    sorted_data = sorted(Dataset, key = lambda item : item['distance'])

    k = 3
    nearest = sorted_data[:k]

    print(Border)
    print("Nearest Neighbours :")
    for d in nearest:
        print(f"{d["point"]} - Distance :", d["distance"])

    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    predicted_class = max(votes, key = votes.get)

    print(Border)
    print("Predicted class :", predicted_class)

    print(Border)

def main():

    KNeighborsClassifier()
    
if __name__ == "__main__":
    main()