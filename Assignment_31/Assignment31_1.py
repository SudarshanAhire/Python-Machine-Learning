# DirectoryFileSearch.py "Demo" ".txt"
import sys
import os
import time

def DirectoryScanner(Directory, Extension):
    Border = "-"*50
    timestamp = time.ctime()
    LogFilename = "Demo%s.log" %(timestamp)
    LogFilename = LogFilename.replace(" ", "_")
    LogFilename = LogFilename.replace(":", "_")

    fobj = open(LogFilename, "w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by Marvellous Automation\n")
    fobj.write("This is a .txt file count script\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.isdir(Directory)

    if(Ret == False):
        print("There is no such directory exists")
        return 
    
    FileCount = 0
    txtExtensionFileCount = 0
    
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            FileCount = FileCount + 1
            fname =  os.path.join(FolderName, fname)

            if(fname.endswith(Extension)):
                txtExtensionFileCount = txtExtensionFileCount + 1
                print(fname)
                fobj.write(fname+"\n")

    fobj.write("Total files scanned :"+str(FileCount)+"\n")
    fobj.write("Total .txt files found :"+str(txtExtensionFileCount)+"\n")
    fobj.write("This log file is created at :"+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()


def main():
    Border = "-"*50
    print(Border)
    print("--------------- Automation Script ----------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return

    Directory = sys.argv[1]
    Extension = sys.argv[2]

    DirectoryScanner(Directory, Extension)

    print(Border)
    print("------------- Automation Script End --------------")
    print(Border)

if __name__ == "__main__":
    main()