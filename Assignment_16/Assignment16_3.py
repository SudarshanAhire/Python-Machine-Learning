def Add(No1, No2):
    return No1 + No2

def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Add(No1, No2)
    print(Ret) 

if __name__ == "__main__":
    main()