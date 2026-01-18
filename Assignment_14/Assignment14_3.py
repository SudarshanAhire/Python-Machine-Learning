
Greater = lambda No1, No2 : No1 > No2

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Greater(No1, No2)

    if(Ret == True):
        print("Greater number is ", No1)
    else:
        print("Greater number is ", No2)

if __name__ == "__main__":
    main()