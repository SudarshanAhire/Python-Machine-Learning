import sys
import os

def CopyData(FileName1, FileName2):
    if(os.path.exists(FileName1)):
        fobj = open(FileName1, "r")

        Data = fobj.read()

        fobj2 = open(FileName2, "w")

        fobj2.write(Data)

        fobj.close()
        fobj2.close()

    else:
        print(f"File {FileName1} is not exists")

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    CopyData(FileName2, FileName2)

if __name__ == "__main__":
    main()

