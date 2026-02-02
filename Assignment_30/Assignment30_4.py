import sys
import os

def CopyData(FileName1, FileName2):
    Ret = False 

    Ret = ((os.path.exists(FileName1)) and (os.path.exists(FileName2)))

    if(Ret == False):
        print("There is no such file in this directory")
        return
    
    fobj1 = open(FileName1, "r")

    Data = fobj1.read()

    fobj2 = open(FileName2, "w")

    fobj2.write(Data)

    fobj1.close()
    fobj2.close()

def main():

    if(len(sys.argv) > 3 or len(sys.argv) < 3):
        print("Invallid Number of arguments")
        return
    
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    CopyData(FileName1, FileName2)

if __name__ == "__main__":
    main()