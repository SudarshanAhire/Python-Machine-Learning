import sys
import os

def Check(FileName, Word):
    Ret = False

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("There is no such file in this directory")
        return 
    
    fobj = open(FileName, "r")

    Data = fobj.read()

    words = Data.split() 

    fobj.close()

    if Word in words:
        return f"The word {Word} is found in {FileName}"
    else:
        return f"The word {Word} is not found in {FileName}"

def main():

    if(len(sys.argv) > 3 or len(sys.argv) < 3):
        print("Invalid number of arguments")
        return
    
    FileName = sys.argv[1]
    Word = sys.argv[2]

    Ret = Check(FileName, Word)
    print(Ret)

if __name__ == "__main__":
    main()