#calculate.py
class Calculate:
    def __init__(self,num1:int,num2:int):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1+self.num2

    def substrat(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1/self.num2
