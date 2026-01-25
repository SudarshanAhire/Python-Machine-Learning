import threading

def DisplayEven():
    for i in range(2, 21):
        if i % 2 == 0:
            print(i)
        
def DisplayOdd():
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)

def main():
    Even = threading.Thread(target=DisplayEven)
    Odd = threading.Thread(target=DisplayOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()    

if __name__ == "__main__":
    main()