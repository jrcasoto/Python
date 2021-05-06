# https://codeforces.com/problemset/problem/231/A
# Problem code 231A

n = int(input())
def team(n):
    s = 0
    for _ in range(n):
        p,v,t = map(int, input().split(' '))
        if p + v + t >= 2:
            s += 1
    return s
print(team(n))