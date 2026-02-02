import sys
import os

def CountWords(FileName):
    Ret = False
    Count = 0

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("No such exists in this directory")
        return 
    
    fobj = open(FileName, "r")

    Data = fobj.read()

    Count = len(Data.split())

    fobj.close()

    return Count 
    

def main():
    FileName = sys.argv[1]

    Ret = CountWords(FileName)
    print(f"Total number of words in {FileName} :", Ret)

if __name__ == "__main__":
    main()