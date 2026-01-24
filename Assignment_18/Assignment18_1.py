def ElementSum(Data):
    Sum = 0

    for i in range(len(Data)):
        Sum = Sum + Data[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter the number of element : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ElementSum(Data)
    print("Addition of all elements : ", Ret)
    


if __name__ == "__main__":
    main()