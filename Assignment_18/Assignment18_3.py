def MinimumElement(Data):
    
    MinElement = Data[0]
    
    for i in range(1, len(Data)):
        if MinElement > Data[i]:
            MinElement = Data[i]

    return MinElement


def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = MinimumElement(Data)
    print("Minimum Element is :", Ret)

if __name__ == "__main__":
    main()