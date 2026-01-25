import threading

def SumEven(No):
    Sum = 0

    for i in range(1, No+1):
        if No % i == 0:
            if i % 2 == 0:
                Sum = Sum + i

    print("Sum od Even :", Sum)

def SumOdd(No):
    Sum = 0

    for i in range(1, No+1):
        if No % i == 0:
            if i % 2 != 0:
                Sum = Sum + i

    print("Sum of Odd :", Sum)

def main():
    No = 0
    No = int(input("Enter number  : "))

    EvenFactor = threading.Thread(target=SumEven, args=(No,))
    OddFactor = threading.Thread(target=SumOdd, args=(No,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")


if __name__ == "__main__":
    main()