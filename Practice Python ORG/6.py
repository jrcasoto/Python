''' Ask the user for a string and print out whether this string is a palindrome
 or not. (A palindrome is a string that reads the same forwards and backwards.)'''
 
# Variable declaration
 
string = str(input("Please insert word here: "))

# One-liner
print("palindrome" if string[::-1] == string[:] else "not palindrome")