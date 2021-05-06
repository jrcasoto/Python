# Problem 04

def getSublists(L, n):
    '''
    Returns an ordered value list according to the specified range n
    L: A non-empty integers list
    n: Integer, assuming thtat 0 < n <= len(L)
    '''
    sublists = []
    for element in range(len(L)):
        if (n + element) <= len(L):
            sublists.append(L[element:(n + element)])
    return print(sublists)


# Test case
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
getSublists(L, 4)
L = [1, 1, 1, 1, 4]
getSublists(L, 2)