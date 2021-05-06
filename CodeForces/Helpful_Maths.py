# https://codeforces.com/problemset/problem/339/A
# Problem code 339A

def helpful_maths(s):
    s.sort()
    output = ''
    for term in s:
        output += str(term) + '+'
    return output[:len(output)-1]

s = list(map(int,input().split('+')))
print(helpful_maths(s))[=]