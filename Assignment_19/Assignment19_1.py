Power = lambda No : 2 ** No

def main():
    No = 0
    Ret = 0

    No = int(input("Enter number : "))

    Ret = Power(No)
    print("Power of 2 is : ", Ret)

if __name__ == "__main__":
    main()