'''https://www.hackerrank.com/challenges/s10-standard-deviation/problem?h_r=next-challenge&h_v=zen'''

import statistics
import math

# Input

n = 5
x = '10 40 30 50 20'
x = list(map(int, x.split()))

# Standard Deviation (mean, square distance from mean and)

m = statistics.mean(x)
sq_dist = float()

for element in x:
    sq_dist += (element-m)**2

print(math.sqrt(sq_dist/int(len(x))))