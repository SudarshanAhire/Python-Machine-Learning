def main():
    No = 0
    No = int(input("Enter Number : "))

    for i in range(1, No+1):
        if i%2 != 0:
            print(i, end=" ")

if __name__ == "__main__":
    main()