# https://codeforces.com/contest/4/problem/B

d, sumTime = map(int,input().split())
schedule = []
highest = 0
t = 0

for day in range(d):
    tmp = []
    minTime, maxTime = map(int,input().split())
    highest += maxTime
    for element in range(minTime, maxTime + 1):
        tmp.append(element)
    schedule.append(tmp)

if highest < int(sumTime):
    print('NO')
else:
    print('YES')
    while t != sumTime:
        for i in schedule:
            t += min(i)
    


def f():
   return list(map(int,input().split()))
d,t=f()
a=[f() for _ in range(d)]
b=list(zip(*a))
zn=sum(b[0])
zx=sum(b[1])
if zn<=t<=zx:
   print('YES')
   delta=t-zn
   for m1,m2 in a:
    today=min(m2-m1,delta)
    delta-=today
    print(m1+max(0,today),end=' ')
else:
    print('NO')