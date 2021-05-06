def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None"""
    l_set = list(set(L))
    l_set2 = list(set(L)) # Can't mutate a list
    for odd in l_set: # Count only for odd numbers
        if L.count(odd) % 2 == 0:
            l_set2.remove(odd)
    l_set2.sort()
    if len(l_set2) == 0:
        return None
    else:
        return l_set2[-1] # Highest
print(largest_odd_times([2,2,4,4]))