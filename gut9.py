#!/usr/bin/python3.8

# import math
# import re
row = []

def GetObj():

    Raw = input ("Please give list of objects : ")
    Organize = Raw.split(" ")
    return (Organize)

def PrtRow(objects):

    ArrLength = len(objects)
    print ("The length of the list is, ", str(ArrLength))
    i = 0
    while i < ArrLength :
          print (objects[i])
          i += 1

print ("This program organizes a list of objects into an array.")
row = GetObj()

PrtRow(row)

