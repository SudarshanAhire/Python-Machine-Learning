def Grade(Marks):
    if Marks > 100 or Marks < 0:
        return "Please enter valid marks"
    
    
    if Marks >= 75:
        return "Distinction"
    elif Marks >= 60:
        return "First Class"
    elif Marks >= 50:
        return "Second Class"
    else:
        return "Fail" 

def main():
    Marks = 0
    Marks = int(input("Enter marks : "))
    Result = Grade(Marks) 
    print("Grade is :", Result)

if __name__ == "__main__":
    main()