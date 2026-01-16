def ChkChar(ch):
    if ch=="a" or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        return "Vowel" 
    elif ch=="A" or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        return "Vowel"
    else:
        return "Consonant"
    

def main():
    ch = None
    ch = input("Enter character : ")
    Result = ChkChar(ch)
    print("The char is : ", Result)

if __name__ == "__main__":
    main()