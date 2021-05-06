''' Given a .txt file that has a list of a bunch of names, count how many of 
each name there are in the file, and print out the results to the screen. I 
have a .txt file for you, if you want to use it!

EXTRA

Instead of using the .txt file from above (or instead of, if you want the 
challenge), take this .txt file, and count how many of each “category” of 
each image there are.'''
'''
# Variable declaration

my_dict = {}

# Conventional way using .txt manipulation

with open(r'Files\22.txt', 'r') as open_file:
    all_text = open_file.read()
    list_names = all_text.split(sep = '\n') #reading lines
    unique_names = set(list_names) #getting unique values from .txt file

for name in unique_names: #appending into empty dictionary
    my_dict[name] = list_names.count(name)

print(my_dict)
'''
# Extra (using pandas)

import pandas as pd
import os

path = r'C:\Users\jcaso\OneDrive\Área de Trabalho\Programming\Python\Practice Python ORG\Files'
os.chdir(path)

df = pd.read_csv('22_extra.txt', header = None)