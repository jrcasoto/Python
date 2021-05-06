# https://codeforces.com/problemset/problem/148/A
# Problem code 148A

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

def dragon(k,l,m,n,d):
    u = 0
    for dragon in range(d):
        if dragon % k != 0 and dragon % l != 0 and dragon % m != 0 and dragon % n != 0:
            u += 0
    return d-u

print(dragon(k,l,m,n,d))