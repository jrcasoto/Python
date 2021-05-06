# https://codeforces.com/problemset/problem/617/A
# Problem code 617A

x = int(input())
def elephant(x):
    s = 0
    e = 5
    while e != 0:
        if x // e > 0:
            s += x // e
            x -= (x // e) * e
        e -= 1
    return s
print(elephant(x))