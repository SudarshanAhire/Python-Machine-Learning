import threading

def Sum(Data):
    Result = 0

    for i in range(len(Data)):
        Result = Result + Data[i]

    print("Sum of list elements is :", Result)

def Product(Data):
    Result = 1

    for i in range(len(Data)):
        Result = Result * Data[i]

    print("Product of list elements is :", Result)

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Thread1 = threading.Thread(target=Sum, args=(Data,))
    Thread2 = threading.Thread(target=Product, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()