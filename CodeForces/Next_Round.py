# https://codeforces.com/problemset/problem/158/A
# Problem code 158A

n,k = map(int, input().split(' '))
g = list(map(int, input().split(' ')))
k = g[k-1]
def next_round(n,k,g):
    s = 0
    for i in g:
        if i >= k and i > 0:
            s += 1
    return s
print(next_round(n,k,g))