# https://codeforces.com/problemset/problem/977/A
# Problem code 977A

n,k = map(int, input().split(' '))

def wrong_subtraction(n,k):
    for k in range(k):
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1
    return int(n)
print(wrong_subtraction(n,k))