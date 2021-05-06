#!/bin/python3

'''https://www.hackerrank.com/challenges/30-2d-arrays/problem'''

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

sums = list()

#Getting values according to indexes
for row in range(0,4):    
    for columns in range(0,4):
        sums.append(arr[row][columns] + arr[row][columns + 1] + arr[row][columns + 2] + arr[row + 1][columns + 1] + arr[row + 2][columns] + arr[row + 2][columns + 1] + arr[row + 2][columns + 2])

print(max(sums))