def is_prime(n):
    if n < 2:
        return True
    else: 
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True

class Primes:        
    def first(n):
        l = []
        i, count = 2, 0
        while count < n:
            if is_prime(i):
                count += 1
                l.append(i)
            i += 1
        print (l)


Primes.first(5)
