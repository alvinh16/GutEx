#!/usr/bin/python3.9

def findroot (x, power, epsilon ):
    print ("x = ", x)
    print ("power = ", power )
    print ("epsilon = ", epsilon)

    if x < 0 and power%2 == 0:
        return None
    low = min (-1.0, x)
    high = max (1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8] :
        for power in range (1, 4) :
            print ("Testing x= ", str(x), "& power = ", power)
            result = findroot(x, power, epsilon)
            if result == None :
                print ("     No root")
            else :
                print ("     ", result**power, "~=" , x )

x = 25
power = 2
epsilon = 0.01

print ("the ans is : ")
print ( findroot (x, power, epsilon) )

testFindRoot()