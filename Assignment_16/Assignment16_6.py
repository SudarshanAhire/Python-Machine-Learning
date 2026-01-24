def ChkNum(No):
    if No == 0:
        return "Zero"
    elif No > 0:
        return "Positive Number"
    else:
        return "Negative Number"

def main():
    No = 0
    No = int(input("Enter number : "))

    Ret = ChkNum(No)
    print(Ret)

if __name__ == "__main__":
    main()