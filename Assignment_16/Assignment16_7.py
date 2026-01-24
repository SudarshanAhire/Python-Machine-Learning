def Divisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    No = 0
    No = int(input("Enter number : ")) 

    Ret = Divisible(No)
    print(Ret)

if __name__ == "__main__":
    main()