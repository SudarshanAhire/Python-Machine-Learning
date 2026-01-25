import threading

def LowerCase(Name):
    Count = 0

    for i in range(len(Name)):
        if str(i) >= str(a) and str(i) <= str(z):
            Count = Count + 1

    print("Small chars : ", Count)

def UpperCase(Name):
    pass

def NumericDigit(Name):
    pass

def main():
    Name =  None
    Name = input("Enter name : ")

    Small = threading.Thread(target=LowerCase, args=(Name,))
    Capital = threading.Thread(target=UpperCase, args=(Name,))
    Digits = threading.Thread(target=NumericDigit, args=(Name))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()