# https://codeforces.com/problemset/problem/236/A
# Problem code 236A

def boy_or_girl(name):
    if len(list(set(name))) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
name = input()
boy_or_girl(name)