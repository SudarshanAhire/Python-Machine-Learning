import os
import sys

def main():
    FileName = sys.argv[1]

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, "r")

        Data = fobj.read()

        fobj1 = open("Demo.txt", "w")

        fobj1.write(Data)

        fobj.close()
        fobj1.close()

if __name__ == "__main__":
    main()