import os 
import sys 

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    if(os.path.exists(FileName1) and os.path.exists(FileName2)):
        fobj1 = open(FileName1, "r")
        fobj2 = open(FileName2, "r")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")

    else:
        print("FIles is not exist")

if __name__ == "__main__":
    main()