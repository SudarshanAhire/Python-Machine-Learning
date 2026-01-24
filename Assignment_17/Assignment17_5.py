def ChkPrime(No):
    if No <= 0 or No == 1:
        return "Not Prime"

    for i in range(2, No):
        if No % i == 0:
            return "It is Not Prime Number"

    return "It is Prime Number"

def main():
    No = 0
    No = int(input("Enter Number : "))

    Ret = ChkPrime(No)
    print(Ret)

if __name__ == "__main__":
    main()