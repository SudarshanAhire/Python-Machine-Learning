import threading

def Prime(Value):
    if Value == 1:
        return False
    
    for i in range(2, Value):
        if Value % i == 0:
            return False
    return True

def NonPrime(Value):
    if Value == 1:
        return True
    
    for i in range(2, Value):
        if Value % i == 0:
            return True
    return False

def DisplayPrime(Data):
    for i in range(len(Data)):
        if Prime(Data[i]) == True:
            print("Prime Numbers :", Data[i])


def DisplayNonPrime(Data):
    for i in range(len(Data))
        if NonPrime(Data[i]) == True:
            print("NonPrime numbers :", Data[i])

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    Prime = threading.Thread(target=DisplayPrime, args=(Data,))
    NonPrime = threading.Thread(target=DisplayNonPrime, args=(Data,))

    Prime.start()
    Prime.join()

    NonPrime.start()
    NonPrime.join()

if __name__ == "__main__":
    main()