# https://codeforces.com/problemset/problem/266/A
# Problem code 266A

n = int(input())
s = input()

def stones(s):
    c = 0
    for i in range(1,len(s)):
        t = s[i]
        if t == s[i-1]:
            c += 1
    return c

print(stones(s))