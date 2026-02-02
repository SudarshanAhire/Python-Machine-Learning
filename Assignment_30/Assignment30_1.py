import sys
import os

def CountLines(FileName):
    Ret = False 
    Count = 0

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("No such file exist in this directory")
        return

    fobj = open(FileName, "r")

    Data = fobj.readlines() 

    for _ in Data:
        Count = Count + 1

    fobj.close()

    return Count     


def main():
    FileName = sys.argv[1]

    Ret = CountLines(FileName)

    if(Ret != None):
        print(f"Total number of lines in {FileName} :", Ret)


if __name__ == "__main__":
    main()