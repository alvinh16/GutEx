#!/usr/bin/python3.9

initval = 10000
currvalue = 92000
stepval = 10000
currate = 0.005 / 12
ratestep = 0.005 / 12
duration = 9
# testval = initval
found = False

while found == False :
    testval = initval
    for i in range (1, duration) :
        testval = (testval * (1+currate)) + stepval
    if testval > currvalue :
        found = True
    print("at rate ", currate*12, "at the end of ", duration, " months, the balance is ", testval)
    currate += ratestep

