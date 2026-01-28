class BankAccount:

    ROI = 10.5

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print(f"Account holder Name is {self.Name} and current balance is {self.Amount}")

    def Deposit(self):
        Amount = float(input("Enter amount for deposit : "))
        self.Amount = self.Amount + Amount

    
    def Withdraw(self):
        Withdraw = int(input("Enter amount for withdraw : "))
        
        if(self.Amount >= Withdraw):
            self.Amount = self.Amount - Withdraw
        else:
            print("Insufficient balance in your acoount")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("ROI on amount :", Interest)
    

obj1 = BankAccount("Sudarshan Ahire", 30000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount("Darshan Ahire", 100000)
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()
