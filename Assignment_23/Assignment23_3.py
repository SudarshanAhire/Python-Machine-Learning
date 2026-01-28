class Numbers:

    def __init__(self, A):
        self.Value = A

    def ChkPrime(self):
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
            
        return True
    
    def ChkPerfect(self):
        FSum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                FSum = FSum + i

        if FSum == self.Value:
            return "Number is perfect"
        else:
            return "Number is not perfect"


    def Factors(self):
        print("Factors of number : ", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0: 
                print(i, end=" ")

    def SumFactors(self):
        FactorSum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                FactorSum = FactorSum + i

        return FactorSum
    
    
Number = int(input("Enter Number : "))

obj1 = Numbers(Number)
print("Number is prime :", obj1.ChkPrime())
print(obj1.ChkPerfect())
obj1.Factors()
print()
print("Sum of factors :", obj1.SumFactors())

print()

Number = int(input("Enter number : "))

obj2 = Numbers(Number)
print("Number is prime :", obj2.ChkPrime())
print(obj2.ChkPerfect())
obj2.Factors()
print()
print("Sum of factors :", obj2.SumFactors())

