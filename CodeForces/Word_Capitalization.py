# https://codeforces.com/problemset/problem/281/A
# Problem code 281A

import string

def cap(word):
    return word[0].upper() + word[1:]
word = input()
cap(word)