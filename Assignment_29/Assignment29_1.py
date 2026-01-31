import os

def main():
    FileName = input("Enter the file name : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print(f"{FileName} exists")

    else:
        print("No such file in this directory")

if __name__ == "__main__":
    main()