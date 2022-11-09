#!/usr/bin/python3.8

# import math
# import re
row = []

def GetObj():

    source_file = open("objectlist.text", "r")
    Organize = source_file.readlines()
    i=0
    for words in Organize : 
        words.rstrip("\r\n")
#        print (words)
        row.extend(words)
        i += 1
    print (row)
    source_file.close()
    return (words)

def PrtRow(objects):

    ArrLength = len(objects)
    print ("The length of the list is, ", str(ArrLength))
    i = 0
    while i < ArrLength :
          print (objects[i])
          i += 1

print ("This program organizes a list of objects into an array.")
row = GetObj()
print (row)

# PrtRow(row)

