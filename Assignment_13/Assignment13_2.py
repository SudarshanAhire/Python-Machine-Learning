def Area(Radius):
    return Radius * Radius * 3.14 

def main():
    Radius  = 0
    Result = 0
    Radius = int(input("Enter radius of circle : "))
    Result = Area(Radius)
    print("Area of circle is : ", Result) 

if __name__ == "__main__":
    main()