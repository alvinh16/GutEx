#!/usr/bin/python3.8

def readVal(ValType, requestMsg, errMsg):

    while True:
        Val = input(requestMsg + " ")
        try:
            return(ValType(Val))
        except ValueError:
            print (Val, errMsg)

readVal(int, "Enter an integer", "is not an integer")
