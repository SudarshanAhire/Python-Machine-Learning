def ChkNum(No):
    if No % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    No = 0
    No = int(input("Enter number : "))

    Ret = ChkNum(No)
    print(Ret) 

if __name__ == "__main__":
    main()