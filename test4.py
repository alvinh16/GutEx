#!/usr/bin/python3.8

# import math
# import re

ArrayLength = 20
# decrease = ArrayLength
base = 0

for decrease in range (1,ArrayLength):
     print ("outer = ", str(decrease))
     for inner in range (decrease,ArrayLength):
          print ("inner = ", str(inner))
     print ()
