# https://codeforces.com/problemset/problem/996/A
# Problem code 996A

c = int(input())

def coins(c):
    q = 0
    for i in [100, 20, 10, 5, 1]:
        q += c // i
        c = c % i
        if c == 0:
            return q
print(coins(c))