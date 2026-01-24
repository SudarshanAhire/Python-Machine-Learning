def DigitCount(No):
    count = 0

    while(No > 0):
        count = count + 1
        No = No // 10
    
    return count


def main():
    No = 0
    No = int(input("Enter Number : "))

    Ret = DigitCount(No)
    print(Ret)

if __name__ == "__main__":
    main()