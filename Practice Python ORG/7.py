''' Given a random list, write one line of Python that takes this list a and 
makes a new list that has only the even elements of this list in it.'''

# Variable declaration
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With filter + lambda
print(list(filter(lambda x: x % 2 == 0, a)))

# With list comprehension
print(list(element for element in a if element % 2 == 0))