def Area(Length, Width):
    return Length * Width 

def main():
    Length = 0
    Width = 0
    Result = 0

    Length = int(input("Enter length : "))
    Width = int(input("Enter Width : "))

    Result = Area(Length, Width) 
    print("Area of rectangle is : ", Result)

if __name__ == "__main__":
    main()