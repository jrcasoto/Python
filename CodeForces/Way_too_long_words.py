# https://codeforces.com/problemset/problem/71/A

n = int(input())
words = []
for i in range(n):
    words.append(input())
def abbreviate(words):
    for word in words:
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            print(word)
abbreviate(words)