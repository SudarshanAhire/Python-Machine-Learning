def ReverseNum(No):
    RevNum = 0

    while( No > 0):
        Digit = No % 10
        RevNum = RevNum * 10 + Digit
        No = No // 10

    return RevNum

def main():
    No = 0
    No = int(input("Enter number : "))
    Result = ReverseNum(No)
    print("Reverse number is : ", Result)

if __name__ == "__main__":
    main()