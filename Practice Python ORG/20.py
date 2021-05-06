''' Write a function that takes an ordered list of numbers (a list where the 
elements are in order from smallest to largest) and another number. The 
function decides whether or not the given number is inside the list and 
returns (then prints) an appropriate boolean.'''

#Variable declaration

a = [1, 3, 5, 30, 42, 43, 500]
b = int(input("Please insert a number: "))

#Declaring function

def isin_func(a,b):
    if len(list(filter(lambda x: x == b, a))) == 0:
        return False
    else:
        return True

#Printing boolean result
print(isin_func(a,b))