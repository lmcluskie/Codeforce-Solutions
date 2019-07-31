import time

t0 = time.time()

def prime_sum(n):
    primes=[2]      
    i=3 
    while i <= n:
        prime = True
        for p in primes:
            if p**2>i:
                break
            if i%p == 0:
                prime = False
        if prime:
            primes.append(i)
        i+=2
    return sum(primes)

print(prime_sum(2000000))
t1 = time.time()
print('Time: ', t1-t0)