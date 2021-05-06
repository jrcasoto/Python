# https://codeforces.com/problemset/problem/791/A
# Problem code 791A

a,b = map(int, input().split(' '))

def big_brother(a,b):
    y = 0
    limak = a
    brother = b
    while limak <= brother:
        y += 1
        limak *= 3
        brother *= 2
    return y

print(big_brother(a,b))