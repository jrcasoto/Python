''' For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. Create a dictionary
(in your file) of names and birthdays. When you run your program it should 
ask the user to enter a name, and return the birthday of that person back to
them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.'''

#Variable declaration

bd_dict = {"Abel": "05/02/2000", "Beto":"01/02/1998"}

#Prompt interface and string manipulation
print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in bd_dict:
    print(name)
lookup = input("Who's birthday do you want to look up? ")

if lookup in bd_dict:
    print(lookup + "'s birthday's date is " + bd_dict[lookup])
else:
    print("Sorry, looks like this name is not on the list!")