''' Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can use 
functions. Make sure to ask the user to enter the number of numbers in the 
sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
where the next number in the sequence is the sum of the previous two numbers 
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

# Iterative

iteration = int(input("Please insert a number: "))
fib_list = [0, 1]


# Declaring function
def fib(iteration):  
    if iteration == 0:
        return False
    else:
        n1 = 0
        n2 = 1
        for i in range(1, iteration + 1):
            fib = n1 + n2
            fib_list.append(fib)
            n1 = n2
            n2 = fib
            
fib(iteration)
print(fib_list)

# Recursive showing the Nth generation number from selected iteration

def fib_rec(iteration):
    # Base cases
    if iteration == 0:
        return 0
    elif iteration == 1:
        return 1
    
    # Recursive case
    else:
        return fib_rec(iteration - 1) + fib_rec(iteration - 2)

print(fib_rec(iteration))