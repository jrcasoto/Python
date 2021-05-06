'''https://projecteuler.net/problem=1'''

from functools import reduce

n = int(input())
l = list()

for i in range(0, n):
    if i % 3 == 0 or i % 5 == 0:
        l.append(i)

print(reduce(lambda x,y: x+y, l))