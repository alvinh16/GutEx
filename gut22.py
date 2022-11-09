#!/usr/bin/python3.8

# import math
# import os
# import re
import datetime

class Person(object):

    def __init__(self, name):

        self.name = name
        try:
            lastBlank = name.rindex(" ")
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

friedrich = Person("Friedrich Der Wise")  
ursala = Person("Ursala Von Derlyen")
christiane = Person("Christiane Legarde")
edmund = Person("Edmund stoiber")
gehard = Person("Gehard Schroeder")
angela = Person("Angela Merkel")
teresa = Person("Teresa May")
martin = Person("martin luther")
siegfried = Person("Siegfried Halle")
haagen = Person("Haagen Holtz")
boris = Person("Boris Johnson")
Francis = Person("Francis Xavier")

print (friedrich.getName())
print (siegfried.getLastName())
