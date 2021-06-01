# https://codeforces.com/problemset/problem/472/A
# Problem code 472A

n = int(input())

def goldbach(n):
    x = int(n / 2)
    f = []
    while (x > 0): # Factoring halves
        p = 2
        if x // p > 1:
            for _ in range(x // p):
                f.append(p)
            x = x % p
        else:
            p += 1
    return f
    


goldbach(n)