# https://codeforces.com/problemset/problem/520/A
# Problem code 520A

n, s= input(), input()
def pangram(s):
    return 'YES' if len(set(s.lower())) == 26 else 'NO'
print(pangram(s))