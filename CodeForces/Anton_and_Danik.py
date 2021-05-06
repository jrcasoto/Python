# https://codeforces.com/problemset/problem/734/A
# Problem code 734A

n = int(input())
s = input()

def winner(s):
    a,d = 0, 0
    for char in s:
        if char == 'A':
            a += 1
        else:
            d += 1
    if a > d:
        return 'Anton'
    elif a < d:
        return 'Danik'
    else:
        return 'Friendship'

print(winner(s))