from fractions import Fraction
try:
    a = Fraction(input("Enter a fraction: "))
    b = Fraction(input("Enter another fraction: "))
except ValueError:
    print ("You entered an invalid number")
except ZeroDivisionError:
    print ("You can't divide by zero")
else:
    print (a+b)

def is_factor (a, b):
    if b % a == 0:
        return True
    else:
        return False


