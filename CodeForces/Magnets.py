# https://codeforces.com/problemset/problem/344/A
# Problem code 344A

n = int(input())

def magnets(n):
    g = 1
    l = []
    for n in range(n):
        m = input()
        l.append(m)
    for n in range(1,n + 1):
        if l[n] != l[n-1]:
            g += 1
    return g

print(magnets(n))