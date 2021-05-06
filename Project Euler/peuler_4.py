'''https://projecteuler.net/problem=4'''

l = list()
def largest_palindrome():
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            conv = list(str(int(i*j)))
            if conv[::-1] == conv:
                l.append(i*j)
largest_palindrome()
print(max(l))