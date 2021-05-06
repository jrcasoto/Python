''' Implement a function that takes as input three variables, and returns the 
largest of the three. Do this without using the Python max() function!'''

#Variable declaration
a = int(input("Please insert number: "))
b = int(input("Please insert number: "))
c = int(input("Please insert number: "))

#Declaring function

def max_three(a,b,c):
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    elif b > c:
        print(b)
    else:
        print(c)

#Calling function
max_three(a,b,c)