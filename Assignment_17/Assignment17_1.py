import Arithmetic

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Addition = Arithmetic.Add(No1, No2)
    print(Addition)

    Subtraction = Arithmetic.Sub(No1, No2)
    print(Subtraction)

    Multiplication = Arithmetic.Mult(No1, No2)
    print(Multiplication)

    Division = Arithmetic.Div(No1, No2)
    print(Division)

if __name__ == "__main__":
    main()