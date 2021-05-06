''' Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

EXTRAS

1. Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. (Hint: order of 
operations exists in Python)

2. Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)'''

 #Get current year
import time
year = int(time.strftime("%Y"))

 #User input
name = input("Please write your name: ")
age = int(input("Please provide your age: "))
#extra 1
mult = int(input("How many times would you like to see the message: "))
 
 #Calculate age dif
def age_dif(age):
    if age <= 100 and age >= 0:
        new_age = year + (100 - age)
        #extra 2
        print(mult * ("You'll be 100 years in year " + str(new_age) + "\n"))
    else:
        print("Invalid age range. Please try again.")

#call function
age_dif(age)