#!/usr/bin/python3.8

# import math
# recursive factorial

def factorial(n):

    if n == 1:
        return n
    else:
        return n * factorial(n-1)

base = 5
target = factorial(base)
print ("factorial of ", base, " is ", str(target))
