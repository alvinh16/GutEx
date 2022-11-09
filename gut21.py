#!/usr/bin/python3.8

class IntSet(object):

    def __init__(self):

        self.vals = []

# inserts e if its not in the list
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)

# Returns True if e is in the list
    def member(self,e):
        return e in self.vals

# removes 1 of the elements in the list
# if the element is no longer there, returns
# error message
    def remove(self,e):
        try:
            self.vals.remove(e)
        except ValueError: 
            print (str(e) + ' not found')

    def getMembers(self):

        return(self.vals[:])

    def __str__(self):

        self.vals.sort()
        result = ""
        for e in self.vals:
            result = result + str(e) + ","

        return "{" + result[:-1] + "}"
s = IntSet()
s.insert(7)
s.insert(2)
s.insert(4)
s.insert(9)
s.insert(5)
# print (s.member(1))
# print (s.member(4))
s.remove(4)
print (s.member(4))
s.remove(4)
print (s.getMembers())
print (s.__str__())
