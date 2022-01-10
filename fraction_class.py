
class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    #The rest goes here
    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

    def reduce(self):
        num, den = self.top, self.bottom
        for i in reversed(range(1, self.top)):
            if num % i == 0 and den % i == 0:
                num = int(num / i)
                den = int(den / i)
        return Fraction (num, den)
    
    def __add__(self, f):
        den = self.bottom * f.bottom
        num = f.top * self.bottom + self.top * f.bottom
        return Fraction(num, den)
        
f = Fraction(3200, 2060)
print(f.reduce())




    
