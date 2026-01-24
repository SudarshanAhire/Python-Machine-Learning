def main():
    No = 0
    No = int(input("Enter Number : "))

    for i in range(No):
        for j in range(No):
            print(" * ", end=" ")
        print()
        No = No -1

if __name__ == "__main__":
    main()