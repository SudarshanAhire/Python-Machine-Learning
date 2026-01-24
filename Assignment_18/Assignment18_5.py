import MarvellousNum

def ListPrime(Data):
    PrimeSum = 0

    for i in range(len(Data)):
        if (MarvellousNum.ChkPrime(Data[i]) == True):
            PrimeSum = PrimeSum + Data[i]
    
    return PrimeSum


def main():
    Size = 0
    Value = 0
    Ret = 0

    Data = list()

    Size = int(input("Enter size of list : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)
    print("Prime number sum is :", Ret)


if __name__ == "__main__":
    main()