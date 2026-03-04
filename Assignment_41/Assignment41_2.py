# import math 

# def EucDistance(P1, P2):
#     Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P2['Y'] - P2['Y']) ** 2)
#     return Ans

# def KNeighboursClassifier():
#     Border = "-"*40

#     Dataset = [
#         {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
#         {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
#         {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
#         {"point" : "D", "X" : 4, "Y" : 5, "label" : "Blue"}
#     ]

#     x_point = int(input("Enter X coordinate : "))
#     y_point = int(input("Enter y coordinate : "))

#     new_point = {"X" : x_point, "Y" : y_point}

#     for d in Dataset:
#         d['distance'] = EucDistance(d, new_point)

#     sorted_data = sorted(Dataset, key = lambda item : item['distance'])

#     k = 1
#     nearest_1 = sorted_data[:k]

#     k = 3
#     nearest_3 = sorted_data[:k]

#     k = 5
#     nearest_5 = sorted_data[:k]

#     print(Border)
#     print("Predicted results ")

#     votes = {}
#     for neighbour in nearest_1:
#         label = neighbour['label']
#         votes[label] = votes.get(label, 0) + 1

#     predicted_class = max(votes, key = votes.get)

#     print("k = 1 -> ", predicted_class)

#     votes = {}
#     for neighbour in nearest_3:
#         label = neighbour['label']
#         votes[label] = votes.get(label, 0) + 1

#     predicted_class = max(votes, key = votes.get)

#     print("k = 3 -> ", predicted_class)

#     votes = {}
#     for neighbour in nearest_5:
#         label = neighbour['label']
#         votes[label] = votes.get(label, 0) + 1

#     predicted_class = max(votes, key = votes.get)

#     print("k = 5 -> ", predicted_class)

#     print(Border)
#     Explanation = """
#     When the value of k increases, more nearest neighbors are considered for voting.

#     k = 1  -> Only 1 neighbor decides the class.
#     k = 3  -> 3 neighbors vote, majority decides.
#     k = 5  -> 5 neighbors vote, majority decides.

#     As k increases, more points influence the decision,
#     so the majority class may change and the final prediction can shift.
#     """

#     print(Explanation)

    
# def main():
#     KNeighboursClassifier() 

# if __name__ == "__main__":
#     main()




import math 

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P2['Y'] - P2['Y']) ** 2)
    return Ans

def Predicted_Class(nearest):
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    predicted_class = max(votes, key = votes.get)

    return predicted_class

def KNeighboursClassifier():
    Border = "-"*40

    Dataset = [
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
        {"point" : "D", "X" : 4, "Y" : 5, "label" : "Blue"}
    ]

    x_point = int(input("Enter X coordinate : "))
    y_point = int(input("Enter y coordinate : "))

    new_point = {"X" : x_point, "Y" : y_point}

    for d in Dataset:
        d['distance'] = EucDistance(d, new_point)

    sorted_data = sorted(Dataset, key = lambda item : item['distance'])

    k = 1
    nearest_1 = sorted_data[:k]

    k = 3
    nearest_3 = sorted_data[:k]

    k = 5
    nearest_5 = sorted_data[:k]

    print(Border)
    print("Predicted results ")

    ret = Predicted_Class(nearest_1)
    print("k = 1 -> ", ret)

    ret = Predicted_Class(nearest_3)
    print("k = 3 -> ", ret)

    ret = Predicted_Class(nearest_5)
    print("k = 5 -> ", ret)

    print(Border)
    Explanation = """
    When the value of k increases, more nearest neighbors are considered for voting.

    k = 1  -> Only 1 neighbor decides the class.
    k = 3  -> 3 neighbors vote, majority decides.
    k = 5  -> 5 neighbors vote, majority decides.

    As k increases, more points influence the decision,
    so the majority class may change and the final prediction can shift.
    """
    
    print(Explanation)

    print(Border)

def main():
    KNeighboursClassifier() 

if __name__ == "__main__":
    main()