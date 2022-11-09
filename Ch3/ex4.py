#!/usr/bin/python3.9

x = 25
epsilon = 0.01
step = epsilon**2
numguesses = 0
low = 0.0
high = max (1.0, x)
ans = (high + low) / 2.0

while abs(ans**2 -x) >= epsilon :
     print("low = ", low, "high = ", high, "ans = ", ans )
     numguesses += 1
     if ans**2 < x :
          low = ans
     else :
          high = ans
     ans = (high + low) / 2.0

print ("Number of guesses = ", numguesses )
print (ans, " is close to the sq root of ", x)
