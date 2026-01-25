Multiplication = lambda A, B : A * B

def main():
    No1 = 0
    No2 = 0
    Ret = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Multiplication(No1, No2)
    print("Multiplication is : ", Ret)

if __name__ == "__main__":
    main()