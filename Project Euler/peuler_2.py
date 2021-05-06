'''https://projecteuler.net/problem=2'''

from functools import reduce

l = [1,2]

def fib(n):
    while l[-1] < 4000000:
            l.append(int(l[-1]+l[-2]))      

fib(n)
l = list(filter(lambda x: x < 4000000, l))

print(int(reduce(lambda x,y: x+y, [i for i in l if i % 2 == 0])))