
Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Minimum(No1, No2)

    print("Minimum number is :", Ret)


if __name__ == "__main__":
    main()