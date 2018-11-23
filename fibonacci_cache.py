from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 1000):
    print(n, ":", fibonacci(n))

