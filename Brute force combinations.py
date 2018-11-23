'''
SEND
+
MORE
----
MONEY
'''

import itertools

for S, E, N, D, M, O, R, Y in itertools.product(range(0, 10), repeat=8):
    if S != 0 and M != 0:
            variables = [S, E, N, D, M, O, R, Y]
            if len(set(variables)) == len(variables):
                if S*1000+E*100+N*10+D + M*1000+O*100+R*10+E == M*10000+O*1000+N*100+E*10+Y:
                    print(" ")
                    print(str(S)+str(E)+str(N)+str(D))
                    print("+")
                    print(str(M)+str(O)+str(R)+str(E))
                    print("-----")
                    print(str(M)+str(O)+str(N)+str(E)+str(Y))
        

    
