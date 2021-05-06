# https://codeforces.com/problemset/problem/116/A
# Problem code 116A

n = int(input())

def tram(n):
    c = 0
    m = 0
    for _ in range(n):
        a, b = map(int, input().split(' '))
        c -= a
        c += b
        if c > m:
            m = c
    return m

print(tram(n))