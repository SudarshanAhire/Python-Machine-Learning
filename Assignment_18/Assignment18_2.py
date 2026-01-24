def MaximumElement(Data):
    MaxElement = Data[0]
    
    for i in range(1, len(Data)):
        if MaxElement < Data[i]:
            MaxElement = Data[i]
            
    return MaxElement


def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter the number of elements : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = MaximumElement(Data)
    print("Maximum element in list is : ", Ret)
    

if __name__ == "__main__":
    main()