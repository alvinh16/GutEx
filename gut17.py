#!/usr/bin/python

import math

def outer(base, height):

    def circle(base):

        area = math.pi * base**2
        volume = 4/3 * math.pi * base**3

        print ("The area of circle is ", area)
        print ("The volume of sphere is ", volume)


    def triangle(base, height):

        area = 1/2 * base * height
        volume = 1/3 * area

        print("The area of triangle is ", area)
        print("The volume of tetrahedron is ", volume)

    print("circle info is")
    circle(base)
    print()
    print("Triangle info is")
    triangle(base,height)
    print()

base = 7.0
height = 5.0
print("the given length is, ", base) 

outer(base, height)
