import os 
import sys

def CountOccurrences(FileName, String)
    if(os.path.exists(FileName)):
        Count = 0
        fobj = open(FileName, "r")

        Ret = fobj.read()

        
        if(Ret == String):
            Count = Count + 1

        return Count
    
    else:
        print("No such file exists")



def main():
    FileName = sys.argv[1]
    String = sys.argv[2]

    Ret = CountOccurrences(FileName, String)
    print(Ret)

    
if __name__ == "__main__":
    main()