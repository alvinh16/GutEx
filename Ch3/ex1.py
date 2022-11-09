#!/usr/bin/python3.9

x = int(input("Enter an integer : "))
ans = 0

print ("the number you gave was, ", x)

while ans**3 < abs(x):
      ans += 1
      print("ans = ", ans)

if ans**3 != abs(x):
     print (x, "is not a perfect cube.")
else:
    if x < 0:
        ans = -ans

print ("The cube root of ", x, " is ", ans)
