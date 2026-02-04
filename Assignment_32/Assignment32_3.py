import sys
import os
import hashlib
import time

def CalculateCheckSum(fname):
    fobj = open(fname, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(Directory): 
    
    Duplicate = {}
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate


def DirectoryDuplicateRemovel(Directory):
    Ret = False

    Ret = os.path.exists(Directory)

    if(Ret == False):
        print("No such directory exists")
        return 
    
    Ret = os.path.isdir(Directory)

    if(Ret == False):
        print("This is not a directory")
        return
    
    MyDict = FindDuplicate(Directory)

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Border = "-"*50
    timestamp = time.ctime()

    fobj = open("Log.txt", "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created using python\n")
    fobj.write("This is a for delete duplicate files\n")
    fobj.write(Border+"\n")
    
    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                fobj.write("Deleted file : "+subvalue+"\n")
                os.remove(subvalue)
                Cnt = Cnt + 1

        Count = 0

    fobj.write("Total duplicate files :"+str(Cnt)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
        
    fobj.close()


def main():

    if(len(sys.argv) != 2):
        print("Invalid number of argumrnts")
        return 
    
    Directory = sys.argv[1]

    DirectoryDuplicateRemovel(Directory)

if __name__ == "__main__":
    main()