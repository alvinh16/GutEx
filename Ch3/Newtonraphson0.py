#!/usr/bin/python3.9

epsilon = 0.01
k = 24.0
guess = k / 2.0
tries = 0

while abs (guess*guess - k ) >= epsilon :
    guess = guess - (((guess**2)-k) / (2 * guess))
    tries += 1

print ("Square root of ", k, "is approximately ", guess, "in ", tries, "iterations.")
