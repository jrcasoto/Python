# https://codeforces.com/problemset/problem/61/A
# Problem code 61A

a = input()
b = input()

def maths(a,b):
    r = ''
    for n in range(len(a)):
        if a[n] == b[n]:
            r += '0'
        else:
            r += '1'
    return r

print(maths(a,b))