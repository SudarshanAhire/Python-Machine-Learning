from functools import reduce

Minimum = lambda No1, No2 : (No1 if No1 < No2 else No2)

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    RData = reduce(Minimum, Data)
    print("Minimum element is :", RData)

if __name__ == "__main__":
    main()