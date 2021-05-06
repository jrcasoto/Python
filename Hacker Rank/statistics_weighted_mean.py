‘’’https://www.hackerrank.com/challenges/s10-weighted-mean/problem’’’

# Input

n = 10
x = '10 40 30 50 20 10 40 30 50 20'
w = '1 2 3 4 5 6 7 8 9 10'

# Organising inputs into lists

x = list(map(int, x.split()))
w = list(map(int, w.split()))

# Weighted mean

w_mean = float()
c = 0

for a in x:
    w_mean += (a * w[c])
    c += 1

# Output
    
print(round(w_mean/sum(w),1))