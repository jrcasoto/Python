'''https://projecteuler.net/problem=3'''

p = 600851475143
l = list()

def primes(p):
    for i in range(1, p+1):
        if p % i == 0:
            l.append(i)
            p = p/i
        if p == 1:
            break

primes(p)
print(l[-1])