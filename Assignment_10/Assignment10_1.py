def PrintTable(No):

    for i in range(1, 11):
        print(No * i, end=" ")

def main():
    No = 0
    No = int(input("Enter number : ")) 
    
    PrintTable(No)

if __name__ == "__main__":
    main()