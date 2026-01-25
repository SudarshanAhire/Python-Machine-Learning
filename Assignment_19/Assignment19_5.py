from functools import reduce

def ChkPrime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Multiply(No):
    return 2 * No

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    Size = 0
    Value = 0

    Data = list()

    Size = int(input("Enter size of list : "))

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkPrime, Data))
    print("List after filter : ", FData)

    MData = list(map(Multiply, FData))
    print("List after map :", MData)

    RData = reduce(Maximum, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()