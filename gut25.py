#!/usr/bin/python3.8

def getRatios(vect1, vect2):

    ratios = []
    for index in range (len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float("nan"))
        except:
            raise ValueError("getRatios called with bad arguments")
    return ratios

try:
    print(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0,0.1]))
except ValueError as msg:
    print(msg)

