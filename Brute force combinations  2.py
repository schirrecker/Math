'''
BLASE
+
LBSA
-----
BASES
'''

import itertools
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
        

    
