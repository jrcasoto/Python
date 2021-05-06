# https://codeforces.com/problemset/problem/705/A
# Problem code 705A

n = int(input())

def hulk(n):
    for i in range(1,n+1):
        if i == n:
            if i % 2 != 0:
                print('I hate it', end=' ')
            else:
                print('I love it', end=' ')
        else:
            if i % 2 != 0:
                print('I hate that', end=' ')
            else:
                print('I love that', end=' ')
    return ''

print(hulk(n))