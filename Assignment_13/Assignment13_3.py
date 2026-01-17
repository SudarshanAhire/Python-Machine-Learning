from functools import reduce  

def ChkPerfect(No):
    Result = list()
    for i in range(1, No):
        Result.append(i)

    FData = list(filter(lambda i : No%i == 0, Result))

    RData = reduce(lambda a, b : a + b, FData)

    return RData

def main():
    No = 0
    No = int(input("Enter number : "))

    Result = ChkPerfect(No)

    if (No == Result):
        print("Perfect Square")
    else:
        print("Not Perfect Square")


if __name__ == "__main__":
    main()