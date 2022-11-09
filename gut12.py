#!/usr/bin/python3.8

# import math
# import re
row = []

def GetObj():

    source_file = open("objectlist.text", "r")
    Organize = source_file.readlines()
    i=0
    for words in Organize : 
        row.append(words.rstrip("\r\n"))
        i += 1
    source_file.close()
    return (row)

def DispRows(objects):

     i = 0
     while i < len(objects):
          print (objects[i])
          i +=1

print ("This program organizes a list of objects into an array.")
row = GetObj()
print (row)
DispRows(row)
