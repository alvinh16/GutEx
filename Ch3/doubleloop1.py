#!/usr/bin/python3.9

initval = 10000
currvalue = 92000
stepval = 10000
ratestep = 0.005 / 12
duration = 9
testval = initval

# while testval < currvalue :

for i in range (1, duration) :
    testval = (testval * (1+ratestep)) + stepval

print ("at the end of ", duration, " months, the balance is ", testval)
