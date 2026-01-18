
ChkLength = lambda name : len(name) > 5

def main():
    Data = ["Sudarshan", "Ahire", "Marvellous", "Computer", "CS", "SITS"]

    FData = list(filter(ChkLength, Data))
    print("List of strings which length is grater then 5 :", FData)

if __name__ == "__main__":
    main()