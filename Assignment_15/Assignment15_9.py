from functools import reduce

Multiplication = lambda No1, No2 : No1 * No2

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    RData = reduce(Multiplication, Data)
    print("Producr of all list elements is :", RData)

if __name__ == "__main__":
    main()