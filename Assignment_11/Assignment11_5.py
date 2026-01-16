def CheckPalindrome(No):
    Copy_No = No
    RevNum = 0

    while(No > 0):
        Digit = No % 10
        RevNum = RevNum * 10 + Digit
        No = No // 10

    if(RevNum == Copy_No):
        return True
    else:
        return False
    

def main():
    No = 0
    Result = 0

    No = int(input("Enter number : "))
    Result = CheckPalindrome(No)
    
    if Result:
        print("Palindrome")
    else:
        print("Not Palindrome")
    

if __name__ == "__main__":
    main()