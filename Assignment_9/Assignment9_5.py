def ChkNum(No):
    if No%3 == 0 and No%5 == 0:
        return True
    else:
        return False
    

def main():
    Result = None
    No = 15
    Result = ChkNum(No)
    
    if(Result == True):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
    
    
if __name__ == "__main__":
    main()