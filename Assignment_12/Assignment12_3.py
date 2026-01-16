def Addition(No1, No2):
    return No1 + No2

def Subtraction(No1, No2):
    return No1 - No2

def Multiplication(No1, No2):
    return No1 * No2

def Division(No1, No2):
    return No1 / No2

def main():
    No1 = 0
    No2 = 0
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    print("Addition is : ", Addition(No1, No2))
    print("Subtraction is : ", Subtraction(No1, No2))
    print("Multiplication is : ", Multiplication(No1, No2))
    print("Division is : ", Division(No1, No2))

if __name__ == "__main__":
    main()