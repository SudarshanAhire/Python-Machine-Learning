
Largest = lambda No1, No2, No3 : (No1 if(No1 > No2 and No1 > No3) else No2 if(No2 > No3) else No3)
# Largest = lambda No1, No2, No3 : max(No1, No2, No3)

def main():
    No1 = 0
    No2 = 0
    No3 = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    No3 = int(input("Enter third number : "))

    Ret = Largest(No1, No2, No3)

    print("Largest number is : ", Ret)

if __name__ == "__main__":
    main()