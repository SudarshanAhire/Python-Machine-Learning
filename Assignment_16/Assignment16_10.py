def Length(Name):
    return len(Name)

def main():
    Name = input("Enter name : ")

    Ret = Length(Name)
    print(Ret)

if __name__ == "__main__":
    main()