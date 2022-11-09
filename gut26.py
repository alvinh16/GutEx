#!/usr/bin/python3.8

def getRatios(vect1, vect2):

    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError("getRatios called with bad arguments")

    for index in range (len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem) not in (int, float)) \
        or (type(vect2Elem) not in (int, float)):
            raise ValueError("getRatios called with bad arguments")
        if vect2Elem == 0.0:
            ratios.append(float("nan"))
        else:
            ratios.append(vect1Elem/vect2Elem)
    return ratios
 
try:
    print(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0,0.1]))
except ValueError as msg:
    print(msg)

