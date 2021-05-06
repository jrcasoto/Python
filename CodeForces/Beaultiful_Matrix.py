# https://codeforces.com/problemset/problem/263/A
# Problem code 263A

m = []
for i in range(5):
    r = list(map(int, input().split(' ')))
    m.append(r)

def b_matrix(m):
    for i in range(5):
        for j in range(5):
            if m[i][j] == 1:
                if i > 2:
                    r = i - 2
                else:
                    r = 2 - i
                if j > 2:
                    c = j - 2
                else:
                    c = 2 - j
                return r + c

print(b_matrix(m))