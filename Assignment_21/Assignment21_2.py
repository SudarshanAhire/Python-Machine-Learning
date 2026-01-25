import threading

def Maximum(Data):
    MaxElement = Data[0]

    for i in range(len(Data)):
        if Data[i] > MaxElement:
            MaxElement = Data[i]
    print("Maximum Element : ", MaxElement)

def Minimum(Data):
    MinElement = Data[0]

    for i in range(len(Data)):
        if Data[i] < MinElement:
            MinElement = Data[i]

    print("Minimum Element : ", MinElement)

def main():
    Size = 0
    Value = 0

    Data = list()

    Size = int(input("Enter Size of list : "))

    for i in range(Size):
        Value =  int(input())
        Data.append(Value)

    Thread1 = threading.Thread(target=Maximum, args=(Data,))
    Thread2 = threading.Thread(target=Minimum, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()