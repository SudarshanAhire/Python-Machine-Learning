import sys
import os

def DisplayLine(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("No such file exists in this directory")
        return
   
    fobj = open(FileName, "r")

    Data = fobj.readlines()

    for line in Data:
        print(line)

def main():

    if(len(sys.argv) > 2 or len(sys.argv) < 2):
        print("Invalid number of arguments")
        return

    FileName = sys.argv[1]

    DisplayLine(FileName)
    

if __name__ == "__main__":
    main()