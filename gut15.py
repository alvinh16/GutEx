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
     return(j)

# the source & destination are swapped
# source (src) is the index to the smallest content in the interval
# destination (dest) is the index to the bottom of the interation 
def SwapCell(src,dest):

     tmpobj = row[src]
     row[src] = row[dest]
     row[dest] = tmpobj

print ("This program organizes a list of objects into an array.")
row = GetObj()
DispRows(row)
print ()
ArrayLength = len(row)

for outer in range (0,ArrayLength):
     print ("outer = ", str(outer))
     for inner in range (outer,ArrayLength):
          minalpha = Smallest(row,outer)
          print (row[minalpha], " = ", str(inner))
          if minalpha != outer : 
               SwapCell(minalpha, outer)
     print ()

print ()
DispRows(row)
# minalpha = Smallest(row,0)
# print (minalpha)
# SwapCell(minalpha, 0)
# DispRows(row)
