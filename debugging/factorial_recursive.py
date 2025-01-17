#!/usr/bin/python3  # Shebang line specifying the Python 3 interpreter

import sys  # Imports the sys module to access command-line arguments

# Defines a recursive function to calculate the factorial of a given number n
def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial of (n - 1)
        return n * factorial(n - 1)

# Reads the first command-line argument, converts it to an integer, and calculates its factorial
f = factorial(int(sys.argv[1]))

# Prints the calculated factorial
print(f)
