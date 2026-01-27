class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Balance = Amount

    def Display(self):
        print(f"Account holder Name is {self.Name} and available balance {self.Balance}")

    def Deposit(self):
        Amount = float(input("Enter amount for deposit : "))
        self.Balance = self.Balance + Amount

    
    def Withdraw(self):
        Withdraw = int(input("Enter amount for withdraw : "))
        
        if(self.Balance >= Withdraw):
            self.Balance = self.Balance - Withdraw
        else:
            print("Insufficient balance in your acoount")

    def CalculateInterest(self):
        Interest = (self.Balance * BankAccount.ROI) / 100
        print("ROI on balance :", Interest)
    

obj1 = BankAccount("Sudarshan", 30000)
obj1.Display()
obj1.Deposit()
obj1.Display()
obj1.Withdraw()
obj1.Display()
obj1.CalculateInterest()
