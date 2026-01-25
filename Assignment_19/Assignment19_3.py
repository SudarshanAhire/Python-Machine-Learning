from functools import reduce

filterX = lambda No : (No >= 70 and No <= 90)

Increment = lambda No : No + 10

Product = lambda No1, No2 : No1 * No2

def main():
    Size = 0
    Value = 0

    Data = list()

    Size = int(input("Enter size of list : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(filterX, Data))
    print("List after filter :", FData)

    MData = list(map(Increment, FData))
    print("List after map :", MData)

    RData = reduce(Product, MData)
    print("Output of Reduce :", RData)


if __name__ == "__main__":
    main()