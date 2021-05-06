''' Write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). Make sure your program works 
on two lists of different sizes.

EXTRAS

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out 
at this point - we’ll get to it soon)'''

# Extra1 : generating randomnly two lists
import random as r

a = []
b = []

# Declaring function
def generate_lists():
    for i in range(1, r.randint(0, 100)):
        a.append(r.randint(0, 100))
    for i in range(1, r.randint(0, 100)):
        b.append(r.randint(0, 100))
        print(a,b)

generate_lists()

# Creating code in one line using filter + lambda
print(set(list(filter(lambda x: x in b, a))))