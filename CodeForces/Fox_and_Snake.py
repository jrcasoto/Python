# https://codeforces.com/problemset/problem/510/A
# Problem code 510A

r, c = map(int, input().split(' '))

def snake(r,c):
    rl = 0
    for i in range(r):
        if i % 2 == 0:
            print('#' * c)
        elif rl == 0:
            rl = 1
            print('.' * (c-1) + '#')
        else:
            rl = 0
            print('#' + '.' * (c-1))
snake(r,c)