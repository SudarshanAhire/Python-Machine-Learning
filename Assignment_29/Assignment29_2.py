import os

def main():
    FileName = input("Enter the file name : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName, "r")
        
        Data = fobj.read()
        print("File content :", Data)

        fobj.close()

    else:
        print("No such file exists in this directory")

if __name__ == "__main__":
    main()