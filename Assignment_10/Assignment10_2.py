def Addition(No):
    Sum = 0

    for i in range(No + 1):
        Sum = Sum + i

    return Sum

def main():
    No = 0
    Sum = 0

    No = int(input("Enter number : "))
    Sum = Addition(No)
    print(Sum)

if __name__ == "__main__":
    main()