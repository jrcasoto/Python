# https://codeforces.com/problemset/problem/785/A
# Problem code 785A

p = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
n = int(input())
def poli(n):
    t = 0
    for _ in range(n):
        i = input()
        t += p[i]
    return t
print(poli(n))