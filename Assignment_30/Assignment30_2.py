import sys
import os

def CountWords(FileName):
    if(os.path.exists(FileName))
        Count = 0

        fobj = open(FileName, "r")

        Ret = fobj.read()

        for _ in Ret:
            if(Ret != " "):
                Count = Count + 1

        fobj.close()

        return Count

    else:
        print("No such file exists in directory")

def main():
    FileName = sys.argv[1]

    Ret = CountWords(FileName)
    print(Ret)

if __name__ == "__main__":
    main()