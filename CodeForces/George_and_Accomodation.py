# https://codeforces.com/problemset/problem/467/A
# Problem code 467A

n = int(input())

def rooms(n):
    a = 0
    for _ in range(n):
        p,q = map(int, input().split(' '))
        if q - p >= 2:
            a += 1
    return a

print(rooms(n))