# Problem 05

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    unique_values = []
    for key, value in aDict.items():
        if list(aDict.values()).count(value) == 1:
            unique_values.append(key)
    
    if len(unique_values) > 0:
        return sorted(unique_values)
    else:
        return unique_values

    

# Test case
uniqueValues({1: 1, 2: 2, 3: 3})
uniqueValues({1: 1, 2: 1, 3: 3})
uniqueValues({})
uniqueValues({5: 1, 7: 1})