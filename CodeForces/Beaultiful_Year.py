# https://codeforces.com/problemset/problem/271/A
# Problem code 271A
import string
y = input()

def b_year(y):
    h = str(int(y) + 1)
    f = True
    while f == True:
        d = '0123456789'
        f = False
        for n in h:
            if n in d:
                d = d.replace(str(n),'')
            else:
                f = True
                break
        h = str(int(h) + 1)
    return int(h)-1
print(b_year(y))