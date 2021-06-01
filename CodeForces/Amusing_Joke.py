# https://codeforces.com/problemset/problem/520/A
# Problem code 141A

a, b, c = input(), input(), input()

def dic(a, b):
    d = {}
    for e in (a+b):
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    return d

d = dic(a, b)

def check(c, d):
    try:
        for e in c:
            if e not in c or d[e] <= 0:
                return 'NO'
            else:
                d[e] -= 1
    except:
        return 'NO'
    for v in d.values():
        if v > 0:
            return 'NO'      
    return 'YES'

print(check(c, d))