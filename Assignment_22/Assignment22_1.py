class Demo:
    Value = 0  # class veriable

    def __init__(self, A, B):
        self.No1 = A 
        self.No2 = B

    def Fun(self):
        print("Inside fun")
        print("Value of No1 :", self.No1)
        print("Value of No2 :", self.No2)

    def Gun(self):
        print("Inside gun")
        print("Value of No1 :", self.No1)
        print("Value of No2 :", self.No2)

obj1 = Demo(10, 11)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()
    
    