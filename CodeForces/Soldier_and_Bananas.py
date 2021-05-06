# https://codeforces.com/problemset/problem/546/A
# Problem code 546A

k,n,w = map(int,input().split(' '))

def bananas(k,n,w):
    s = 0
    for b in range(1,w+1):
        s += k*b
    if s - n < 0:
        return 0
    else:
        return s - n

print(bananas(k,n,w))