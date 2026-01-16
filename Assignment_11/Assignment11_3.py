def DigitSum(No):
    Sum = 0

    while(No >= 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No / 10

    return Sum


def main():
    No = 0
    No = int(input("Enter Number : "))

    Result = DigitSum(No)
    print(Result) 

if __name__ == "__main__":
    main()