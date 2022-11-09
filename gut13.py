#!/usr/bin/python3.8

# import math
# import re
row = []

# This func reads the file containing a list of objects,
# dumps the contents into the list row
# & returns row.
def GetObj():

    source_file = open("objectlist.text", "r")
    Organize = source_file.readlines()
    i=0
    for words in Organize : 
        row.append(words.rstrip("\r\n"))
        i += 1
    source_file.close()
    return (row)

# This func displays the content of objects
def DispRows(objects):

     i = 0
     while i < len(objects):
          print (objects[i])
          i +=1

# This func starts searching from position pos &
# returns the position of the smallest object
def Smallest(objects, pos):

     i = pos
     j = i
     while i < len(objects):
          if objects[i] < objects[j] : 
               j = i
               print(objects[j])
          i += 1

     return(objects[j])

print ("This program organizes a list of objects into an array.")
row = GetObj()
print (row)
DispRows(row)
print ()
MinAlpha = Smallest(row,0)
print (MinAlpha)
