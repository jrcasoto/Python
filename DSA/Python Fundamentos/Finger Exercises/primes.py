n = int(input())
def goldbach(n):
    l = [x for x in range(2,(n+1))]
    return list(filter(lambda num: all(num % r != 0 for r in range(2,num)) == True , l))
print(goldbach(n))