def FactSum(No):
    Sum = 0
    
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum 

def main():
    No = 0
    No = int(input("Enter Number : "))

    Ret = FactSum(No)
    print(Ret)

if __name__ == "__main__":
    main()