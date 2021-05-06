# https://codeforces.com/problemset/problem/469/A
# Problem code 469A

n = int(input())
p, q = [], []
p = (list(map(int,input().split())))[1:]
q = (list(map(int,input().split())))[1:]
print('I become the guy.' if len(set(p + q)) == n else 'Oh, my keyboard!')