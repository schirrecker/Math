tab = 0
def factorial(n):
    # global tab
    # tab += 1
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)


print (factorial(4))

    
