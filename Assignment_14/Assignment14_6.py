
Odd =  lambda No1 : (No1 % 2 != 0)

def main():
    No1 = 0

    No1 = int(input("Enter number : "))

    Ret = Odd(No1)

    print(Ret)

if __name__ == "__main__":
    main()