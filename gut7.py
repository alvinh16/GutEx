#!/usr/bin/python3.8

import math
import re
# import numpy as np

def bigger (a, b):

     if a > b :
        return a
     else :
        return b

x = input("Please enter the first comparion : ") 
y = input("Please enter the second comparion : ") 

print("the larger number is ", bigger(x,y)) 
