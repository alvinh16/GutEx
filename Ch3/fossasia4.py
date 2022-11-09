#!/usr/bin/python3.9

factorial = 20
product = 1

for i in range (factorial, 0, -1):
    print ("i = ", i)
    product *= i

print (product)