# https://codeforces.com/problemset/problem/59/A
# Problem code 59A

import string

s = input()

def word(s):
    l = 0
    u = 0
    for letter in s:
        if letter.islower() == True:
            l += 1
        else:
            u += 1
    if l >= u:
        return s.lower()
    else:
        return s.upper()

print(word(s))