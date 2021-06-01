# https://codeforces.com/problemset/problem/750/A
# Problem code 750A

n, k = map(int, input().split(' '))

def prob(n, k):
    t = 240 - k
    p = 0
    for i in range(1, (n + 1)):
        t -= (i * 5)
        if t >= 0:
            p += 1
        else:
            return p
    return p

print(prob(n, k))