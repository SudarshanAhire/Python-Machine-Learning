Divisible = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Data = [23, 54, 76, 98, 66, 55, 90, 87, 65, 45]

    FData = list(filter(Divisible, Data))
    print("List of divisible by 3 and 5 is :", FData)

if __name__ == "__main__":
    main()