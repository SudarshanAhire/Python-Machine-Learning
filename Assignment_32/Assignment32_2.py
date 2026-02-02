import sys
import os
import hashlib

def CalculateCheckSum(fname):
    fobj = open(fname, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def DirectoryDuplicate(Directory):
    Ret = False

    Ret = os.apth.exists(Directory)

    if(Ret == False):
        print("There is no such directory exists")
        return 
    
    Ret = os.path.isdir(Directory)

    if(Ret == False):
        print("This is not a directory")
        return
    
    MyDict = {}
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            fname = os.path.join(FolderName, FileName)

            CheckSum = CalculateCheckSum(fname)

            if CheckSum in MyDict.values():
                MyDict[CheckSum].apppend(fname)
            else:
                MyDict[CheckSum] = [fname]


    return MyDict


def FilterDuplicate(MyDict):
    pass    

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        return
    
    Directory = sys.argv[1]

    DirectoryDuplicate(Directory)


if __name__ == "__main__":
    main()