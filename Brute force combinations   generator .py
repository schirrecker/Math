'''
BLASE
+
LBSA
-----
BASES
'''

import itertools

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

code = "BLASE+LBSA=BASES"
letters = list(code.split())

def strAlpha(text):
    str = ""
    for l in text:
        if l in ALPHABET:
            str += l
    return str

def numberUniqueLetters(text):
    return len(set(strAlpha(code)))

def varLetters(text):
    letterSet = set(strAlpha(code))
    return list(letterSet)

def varDict(text):
    d = {}
    for l in varLetters(code):
        d[l]=0
    return d
    

variable3 = code.split("=")[1]
variable1 = (code.split("=")[0]).split("+")[0]
variable2 = (code.split("=")[0]).split("+")[1]

print(variable1)
print (variable2)
print (variable3)
print (varLetters(code))
print (varDict(code))




### tup = tuple((element.foo, element.bar) for element in alist)
'''
for B, L, A, S, E in itertools.product(range(0, 10), repeat=5):
    if B != 0 and L != 0:
            variables = [B, L, A, S, E]
            if len(set(variables)) == len(variables):
                if B*10000+L*1000+A*100+S*10+E + L*1000+B*100+S*10+A == B*10000+A*1000+S*100+E*10+S:
                    print(" ")
                    print(str(B)+str(L)+str(A)+str(S)+str(E))
                    print("+")
                    print(str(L)+str(B)+str(S)+str(A))
                    print("-----")
                    print(str(B)+str(A)+str(S)+str(E)+str(S))
        
'''
    
