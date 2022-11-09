#!/usr/bin/python3.8

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

base = 2
supscr = 3

ans = power(base, supscr)
print(base, "to the power of ", supscr, " is ", str(ans)) 
