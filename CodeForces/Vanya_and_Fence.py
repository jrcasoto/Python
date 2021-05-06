# https://codeforces.com/problemset/problem/677/A
# Problem code 677A

n,f = map(int, input().split(' '))
h = list(map(int, input().split(' ')))

def fence(n,f,h):
    w = 0
    for p in h:
        if p > f:
            w += 2
        else:
            w += 1
    return w

print(fence(n,f,h))