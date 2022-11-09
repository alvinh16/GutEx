#!/usr/bin/python3.9

import math

num = input ("what number would u like? ")
print ("you entered " + str(num))
# print (type (num))

if int(num)%2 == 0:
    print (str(num) + " is an even number.")
else : 
    print (str(num) + " is an odd number.")
