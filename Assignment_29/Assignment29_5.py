import sys
import os

def CountOccurences(FileName, String):
    Ret = False
    Count = 0

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("No such file in this directory")
        return
    
    fobj = open(FileName, "r")

    Data = fobj.read()

    fobj.close()

    Count = Data.count(String)

    return Count

def main():

    FileName = sys.argv[1]
    String = sys.argv[2]

    Count = CountOccurences(FileName, String)

    print(f"{Count} times {String} appears in {FileName}")

if __name__ == "__main__":
    main()








