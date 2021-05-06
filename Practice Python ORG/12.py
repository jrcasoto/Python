''' Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first 
and last elements of the given list. For practice, write this code inside a
function.'''

#Variable declaration
a = [5, 10, 15, 20, 25]

#Declaring function
def first(a):
    print(a[0])
    
def last(a):
    print(a[len(a)-1])
    
#Calling functions
first(a)
last(a)