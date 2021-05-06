''' Given an array list, write a program that prints out all the elements of 
the list that are less than 5.

EXTRAS

1. Instead of printing the elements one by one, make a new list that has all
the elements less than 5 from this list in it and print out this new list.

2. Write this in one line of Python.

3. Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the user.'''

#Variable declaration
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input("Type upper limit number: "))

#Solution in one line of code using filter + lambda
print(list(filter(lambda x: x < num, a)))
b = list(filter(lambda x: x < num, a))

#Or list comprehension
print(list(x for x in a if x < num))
b = list(x for x in a if x < num)