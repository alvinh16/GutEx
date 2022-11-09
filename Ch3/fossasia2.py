#!/usr/bin/python3.9

a = 10
b = 20
c = 15

max = a

for test in (a, b, c) :
    if test > max :
        max = test

print ("the max is", max)