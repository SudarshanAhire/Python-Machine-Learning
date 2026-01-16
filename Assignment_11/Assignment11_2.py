def CountDigit(No):
    Count = 0

    while No > 0:
        No = No //10
        Count = Count + 1

    return Count     

def main():
    No = 0
    Result = None

    No = int(input("Enter Number : "))
    Result = CountDigit(No)
    print("Count of digits : ", Result)

if __name__ == "__main__":
    main()