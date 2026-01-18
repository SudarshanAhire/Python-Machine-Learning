def Factorial(No):
    Result = 1

    for i in range(1, No+1):
        Result = Result * i

    return Result 

def main():
    No = 0
    Result = 0

    No = int(input("Enter number : "))
    Result = Factorial(No)
    print(Result)

if __name__ == "__main__":
    main()