# https://codeforces.com/problemset/problem/282/A
# Problem code 282A

n = int(input())
def bit(n):
    x = 0
    for n in range(n):
        b = input()
        if b[-2] == '-':
            x -= 1
        else:
            x += 1
    return x
print(bit(n))