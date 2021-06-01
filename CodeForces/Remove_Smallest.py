# https://codeforces.com/problemset/problem/1399/A
# Problem code 1399A

def smallest():
    l = list(set(map(int, input().split(' '))))
    if len(l) == 0:
        return 'NO'
    else:
        l.sort()
        s = l.copy()
        for i in range(len(l)-1):
            try:
                if abs(l[i]-l[i+1]) == 1:
                    if l[i] > l[i+1]:
                        s.remove(l[i+1])
                    else:
                        s.remove(l[i])
            except:
                pass
    if len(s) == 1:
        return 'YES'
    else:
        return 'NO'


n = int(input())
o = []
for _ in range(n):
    f = input()
    o.append(smallest())
for a in o:
    print(a)