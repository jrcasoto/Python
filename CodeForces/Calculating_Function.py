# https://codeforces.com/problemset/problem/486/A
# Problem code 486A

n = int(input())

def f(n):
    return n // 2 - n % 2 * n

print(f(n))