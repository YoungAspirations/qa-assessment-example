    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
    
import py


def endsPy(input):
    if str.lower(input[-2:]) == 'py':
        return True
    else:
        return False

    
# <QUESTION 2>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter

# <EXAMPLES>

# one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) → {'apple':3, 'orange':2, 'banana':1}
# one(['tic', 'tac', 'toe']) → {'tic':1, 'tac':1, 'toe':1}

   
#def one(items):
  
    #pass

# <QUESTION 3>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

# <EXAMPLES>

# two(2, 4, '+') → 6
# two(7, 3, '-') → 4
# two(3, 1.5, '*') → 4.5
# two(-5, 2, '/') → -2.5

def two(a, b, operator):
    if operator == '/':
        solution = a/b
    elif operator == '*':
        solution = a*b
    elif operator == '+':
        solution = a+b
    elif operator == '-':
        solution = a-b
    else:
        return 'error'
    return solution
    
    #pass

# <QUESTION 4>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <EXAMPLES>

# three(7) → 4          # 4 is the square of 2
# three(64) → 64        # 64 is the square of 8 already
# three(32) → 25

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):
    for i in range(num):
        i += 1
        v = num -i
        if (v**0.5) == int():
            return v

    #pass

# <QUESTION 5>

# Given two integers, return the greatest common factor of the two numbers

# <EXAMPLES>

# four(32, 24) → 8
# four(18, 11) → 1
# four(10, 50) → 10

def four(a, b):
    c = []
    d = []
    g = []
    for i in range(a):
        i+=1
        c.append(a/i)
    for i in range(b):
        i+=1    
        d.append(b/i)
    for i in c:
        if i in d:
            g.append(i)
    hcf = max(g, default = 0)
    return hcf
    pass

# <QUESTION 6>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

# <EXAMPLES>

# five('wxyz') → 'vwxy'
# five('abc') → 'zab'
# five('aAbB') → 'zZaA'
# five('hello world') → 'gdkkn vnqkc'
# five('54321') → '54321'

def five(string):
    pass
