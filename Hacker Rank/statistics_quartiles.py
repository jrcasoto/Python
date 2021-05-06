'''https://www.hackerrank.com/challenges/s10-quartiles/problem'''

import statistics
import math
# Input

n = int(input())
x = input()

x = list(map(int, x.split()))

# Median/Q2
q2 = statistics.median(x)

# Q1/Q3

l_limit = list()
u_limit = list()

# Check index of median
index = float()

if (len(x)/2) % 2 == 0:
    index = (len(x)/2)
    l_limit = x[0:index+1]
    u_limit = x[index:len(x)+1]

else:
    index = (math.ceil(len(x)/2))
    l_limit = x[0:index-1]
    u_limit = x[index-1:len(x)+1]

q1 = statistics.median(l_limit)
q3 = statistics.median(u_limit)
 
print(int(q1))
print(int(q2))
print(int(q3))