# https://codeforces.com/problemset/problem/110/A
# Problem code 110A

n = input()

def lucky(n):
    s = 0
    for e in range(len(n)):
        if int(n[e]) == 4 or int(n[e]) == 7:
            s += 1
    if s == 4 or s == 7:
        return 'YES'
    else:
        return 'NO'
print(lucky(n))