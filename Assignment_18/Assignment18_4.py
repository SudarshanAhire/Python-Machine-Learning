def FrequencyCount(Data, No):
    Count = 0

    for i in range(len(Data)):
        if Data[i] == No:
            Count = Count + 1

    return Count

def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter the number of elements : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Enter number which you want to search in list : ")
    No = int(input())

    Ret = FrequencyCount(Data, No)
    print("Frequency Count of No is : ", Ret)

if __name__ == "__main__":
    main()