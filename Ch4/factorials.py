#!/usr/bin/python3.9

def facti(n):

    result = 1
    while n > 1 :
        result = result * n
        n -= 1
    return result

def factr(n):

    if n == 1 :
        return n
    else :
        return n * factr(n-1)

factorialtype = input ("which factorial would you like? (i)terative or (r)ecursive : ")
base = input ("what is the factorial base?  ")
print ("The factorial of ", base, "is")

if factorialtype == "i" :
     ans = facti (int(base))
     print (ans)
elif factorialtype == "r":
     ans = factr (int(base))
     print (ans)
else :
     print ("not a valid factorial type")
