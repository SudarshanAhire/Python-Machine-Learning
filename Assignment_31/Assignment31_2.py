# python Assignment31_2.py Demo .doc .py

import sys
import os
import time

def DirectoryRename(Directory, Extension1, Extension2):
    Border = "-"*50
    timestamp = time.ctime()
    LogFilename = "Demo%s.log" %(timestamp)
    LogFilename = LogFilename.replace(" ", "_")
    LogFilename = LogFilename.replace(":", "_")

    fobj = open(LogFilename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This is to change extension of file\n")
    fobj.write(Border+"\n")


    Ret = False 

    Ret = os.path.isdir(Directory)

    if(Ret == False):
        print("There isno such directory exists")
        return 
    
    FileCount = 0
    ChangeFileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            FileCount = FileCount + 1
            fname =  os.path.join(FolderName, fname)

            if fname.endswith(Extension1):
                ChangeFileCount = ChangeFileCount + 1
                file, ext = os.path.splitext(fname)
                NewName = file + Extension2
                os.rename(fname, NewName)

    fobj.write("Total files scanned :"+str(FileCount)+"\n")
    fobj.write("Total files extension changed :"+str(ChangeFileCount)+"\n")
    fobj.write("This log file is created at :"+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()
                

def main():
    
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        return
    
    Directory = sys.argv[1]
    Extension1 = sys.argv[2]
    Extension2 = sys.argv[3]

    DirectoryRename(Directory, Extension1, Extension2)


if __name__ == "__main__":
    main()