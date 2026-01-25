from functools import reduce 

ChkEven = lambda No : (No % 2 == 0)

Square = lambda No : No * No

Addition = lambda No1, No2 : No1 + No2

def main():
    Size = 0
    Value = 0

    Data = list()

    Size = int(input("Enter size of list : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkEven, Data))
    print("List after filter : ", FData)

    MData = list(map(Square, FData))
    print("List After map : ", MData)

    RData = reduce(Addition, MData)
    print("Output of reduce :", RData)


if __name__ == "__main__":
    main()