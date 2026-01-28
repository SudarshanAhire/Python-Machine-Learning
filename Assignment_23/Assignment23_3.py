class Numbers:

    def __init__(self, A):
        self.Value = A

    def ChkPrime(self):
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
            
        return True
    
    def ChkPerfect(self):
        # FSum = 0
        # for i in range(1, self.Value):
        #     if self.Value % i == 0:
        #         FSum = FSum + i

        FSum = self.SumFactors()

        if FSum == self.Value:
            return "Number is perfect"
        else:
            return "NUmber is not perfect"


    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0: 
                print(i, end=" ")

    def SumFactors(self):
        FactorSum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                FactorSum = FactorSum + i

        return FactorSum
    

obj1 = Numbers(int(input("Enter number : ")))
print(obj1.ChkPrime())
print(obj1.ChkPerfect())
obj1.Factors()
print()
print(obj1.SumFactors())

