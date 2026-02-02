import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def CompareContent(FileName1, FileName2):
    Ret = False
    
    Ret = ((os.path.exists(FileName1)) and (os.path.exists(FileName2)))

    if(Ret == False):
        print("No such files in this directory")
        return
    
    F1CheckSum = CalculateCheckSum(FileName1)
    F2CheckSum = CalculateCheckSum(FileName2)

    if(F1CheckSum == F2CheckSum):
        return "Success"
    else:
        return "Failure"

def main():

    if(len(sys.argv) < 3 or len(sys.argv) > 3):
        print("Invalid number of arguments")
        return

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    Ret = CompareContent(FileName1, FileName2)
    print(Ret)

if __name__ == "__main__":
    main()
