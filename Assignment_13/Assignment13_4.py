"""Write a program which accepts one 
 numner and and print binary equivalent"""

def Binary(No):
    Result = ""

    while No > 0:
        Result = str(No%2) + Result
        No = No // 2

    return Result

def main():
    No = 0
    No = int(input("Enter number : "))
    Ret = Binary(No)
    print("Binary equivalent of number is : ", Ret) 

if __name__ == "__main__":
    main()