# https://codeforces.com/problemset/problem/50/A
# Problem code 50A

def dominoes(m,n):
    return m * n // 2
m,n = map(int,input().split(' '))
print(dominoes(m,n))