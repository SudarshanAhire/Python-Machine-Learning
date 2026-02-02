import sys
import os
import time

def DirectoryCopy(Directory1, Directory2):

    Border = "-"*50
    timestamp = time.ctime()
    LogFilename = "Demo%s.log" %(timestamp)
    LogFilename = LogFilename.replace(" ", "_")
    LogFilename = LogFilename.replace(":", "_")

    fobj = open(LogFilename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This is to copy file to another directory\n")
    fobj.write(Border+"\n") 

    Ret = False

    Ret = os.path.isdir(Directory1)

    if(Ret == False):
        print("There is no such directory exists")
        return
    
    os.makedirs(Directory2)

    FileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(Directory1):

        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            FileCount = FileCount + 1
            print(fname)

            if os.path.isfile(fname):

                folder = os.path.join(Directory2, os.path.basename(fname))

                fobj1 = open(fname, "r")
                Data = fobj1.read()

                fobj2 = open(folder, "w")

                fobj2.write(Data)

                fobj1.close()
                fobj2.close()

    fobj.write("Total files Copied :"+str(FileCount)+"\n")
    fobj.write("This log file is created at :"+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()
                

def main():

    Border = "-"*50
    print(Border)
    print("------------- Python Automaton Script ------------")
    print(Border)
    
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    Directory1 = sys.argv[1]
    Directory2 = sys.argv[2]

    DirectoryCopy(Directory1, Directory2)

    print(Border)
    print("----------- Python Automaton Script End ----------")
    print(Border)

if __name__ == "__main__":
    main()