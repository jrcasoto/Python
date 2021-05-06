# https://codeforces.com/problemset/problem/112/A
# Problem code 112A

s1 = input()
s2 = input()
def lexico(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(len(s1)):
        if ord(s1[i]) > ord(s2[i]):
            return 1
        elif ord(s1[i]) < ord(s2[i]):
            return -1
    return 0

print(lexico(s1,s2))