# https://codeforces.com/contest/4/problem/A

w = int(input())

def watermelon(w):
    even = []
    for i in range(2, w, 2):
        even.append(i)
    for i in even:
        for j in even:
            if i + j == w:
                return print('YES')
    return print('NO')

watermelon(w)