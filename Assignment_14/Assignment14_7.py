
Divisible = lambda No : (No % 5 == 0)

def main():
    No = 0

    No = int(input("Enter number : "))

    Ret = Divisible(No)

    print(Ret)

if __name__ == "__main__":
    main()