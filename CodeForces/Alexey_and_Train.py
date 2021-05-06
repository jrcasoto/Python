# https://codeforces.com/problemset/problem/1501/A

''' n stations, 
    (ai, bi), where:
        ai = arrival time on the ith station,
        bi = departure time on the ith station
    tmi - extra time to travel between stations
    time to travel is ai-(bi-1)+tmi, where if i=1 then b0 is the moment the train leave the terminal, so equal to 0
    '''
t = int(input()) # number of test cases
n = int(input()) # number of stations
for _ in range(n):
    a, b = map(int(), input().split(' '))