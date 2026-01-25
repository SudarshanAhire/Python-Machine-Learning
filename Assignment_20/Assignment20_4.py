import threading

def LowerCase(Name):
    Count = sum(1 for ch in Name if ch.islower())
    print("Lowercase count :", Count)
    print("LowerCase Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

def UpperCase(Name):
    Count = sum(1 for ch in Name if ch.isupper())
    print("Uppercase count :", Count)
    print("UpperCase Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

def NumericDigit(Name):
    Count = sum(1 for ch in Name if ch.isdigit())
    print("Numeric digit count :", Count)
    print("Numeric Digit Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

def main():
    Name =  None
    Name = input("Enter name : ")

    Small = threading.Thread(target=LowerCase, args=(Name,), name = "Small")
    Capital = threading.Thread(target=UpperCase, args=(Name,), name = "Capital")
    Digits = threading.Thread(target=NumericDigit, args=(Name,), name = "Digits")

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

if __name__ == "__main__":
    main()