# python Assignment32_1.py Demo

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

def DirectoryCheckSum(Directory):
    Ret = False 

    Ret = os.path.exists(Directory)

    if(Ret == False):
        print("Directory does not exists")
        return
    
    Ret = os.path.isdir(Directory)

    if(Ret == False):
        print("This is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            print(CheckSum)

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        return

    Directory = sys.argv[1]

    DirectoryCheckSum(Directory)

if __name__ == "__main__":
    main()