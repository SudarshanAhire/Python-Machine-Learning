def Cube(No):
    return No * No * No

def main():
    Result = 0
    No = int(input("Enter number : "))
    Result = Cube(No)
    print(Result)

if __name__ == "__main__":
    main()