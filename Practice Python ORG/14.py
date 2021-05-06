''' Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the list minus all the duplicates.

EXTRAS

1. Write two different functions to do this - one using a loop and constructing 
a list, and another using sets.'''

import random as r

a = []

# Declaring random list generator function
def generate_lists():
    for i in range(1, r.randint(0, 100)):
        a.append(r.randint(0, 100))
    print(a)

generate_lists()

# Declaring lists comparison function

def lists_comparison(a):
    print(set(a))
    
lists_comparison(a)