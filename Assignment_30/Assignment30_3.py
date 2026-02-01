import sys
import os

def DisplayLine(FileName):
    if(os.path.exists(FileName)):
        fobj = open(FileName, "r")

        Ret = fobj.readlines()

        for line in Ret:
            print(line)

    else:
        print("No such file exists")

def main():

    FileName = sys.argv[1]

    DisplayLine(FileName)
    

if __name__ == "__main__":
    main()