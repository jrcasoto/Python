# https://codeforces.com/contest/4/problem/C

n = input()
names = []
prompt = []
for n in range(int(n)):
    counter = 0
    user = input()
    tmp = user
    if user not in names:
        names.append(user)
        prompt.append('OK')
    else:
        while tmp in names:
            counter += 1
            tmp = str(counter)
            tmp = user + tmp
        prompt.append(tmp)
        names.append(tmp)
for message in prompt:
    print(message)