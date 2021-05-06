# Problem 06

def sumDigits(N):
    '''
    Calculates and returns the sum of its digits (recursively)
    N: A non-negative number
    '''
    if N == 0:
        return 0
    else:
        return N % 10 + sumDigits(N//10)

# Test Case
print(sumDigits(25))