#!/usr/bin/python3.9

x = 25
epsilon = 0.01
step = epsilon**2
numguesses = 0
ans = 0.0

while abs(ans**2 -x) >= epsilon and ans <= x:
     ans += step
     numguesses += 1

print ("Number of guesses = ", numguesses )
if abs(ans**2 -x) >= epsilon:
     print("Failed on sq root of ", x)
else:
     print (ans, " is close to the sq root of ", x)
