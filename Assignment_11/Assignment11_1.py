def CheckPrime(No):
    if No <= 0 or No == 1:
        return False

    for i in range(2, No):
        if No%i == 0:
            return False
        
    return True

def main():
    No = 0
    No = int(input("Enter Number : "))
    Result = CheckPrime(No)

    if Result:
        print("Prime Number")
    else:
        print("Not Prime")

if __name__ == "__main__":
    main()