def factorial(x):
    r = 1
    for i in range(1,x):
        r *= i+1
    return r

print(factorial(9))
