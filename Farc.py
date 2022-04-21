
class fraction:
    def __init__(self,input1,input2,input3,input4):
        self.numerator = input1
        self.denominator = input2
        self.numerator2 = input3
        self.denominator2 = input4
    def add (self):
        a = (self.numerator*self.denominator2)+(self.denominator*self.numerator2)
        b=  self.denominator*self.denominator2
        c = a / b
        print ("Add:",c)
    def sub (self):
        a = (self.numerator*self.denominator2)-(self.denominator*self.numerator2)
        b=  self.denominator*self.denominator2
        c = a / b
        print ("Sub:",c)
    def mul (self):
        a = self.numerator*self.numerator2
        b=  self.denominator*self.denominator2
        c = a / b

        print ("Mul:",c)
    def div (self):
        a = self.numerator*self.denominator2
        b=  self.denominator*self.numerator2
        c = a / b
        print ("Div:",c)
    def show (self):
        classrunner.add()
        classrunner.sub()
        classrunner.mul()
        classrunner.div()

classrunner = fraction (7,3,6,2)
classrunner.show()
