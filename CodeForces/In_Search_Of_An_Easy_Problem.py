# https://codeforces.com/problemset/problem/1030/A
# Problem code 1030A

n = int(input())

def easy():
    return 'HARD' if sum(list(map(int,input().split()))) > 0 else 'EASY'

print(easy())