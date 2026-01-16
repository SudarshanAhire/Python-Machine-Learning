def Factorial(No):
    if No == 0 or No == 1:
        return 1
    
    Result = No * Factorial(No-1) 

    return Result 

def main():
    No = 0
    Result = 0

    No = int(input("Enter number : "))
    Result = Factorial(No)
    print(Result)

if __name__ == "__main__":
    main()