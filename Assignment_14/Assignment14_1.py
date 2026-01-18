
Square = lambda No : No * No

def main():
    No = 0
    
    No = int(input("Enter number : "))

    Ret = Square(No)
    
    print("Square is :", Ret)

if __name__ == "__main__":
    main()