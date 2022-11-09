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

    def setBirthday(self, birthdate):
        self.birthday = birthdate

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name
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

friedrich.setBirthday(datetime.date(1382, 8, 4))
ursala.setBirthday(datetime.date(1962, 3, 15))
christiane.setBirthday(datetime.date(1958, 8, 5))
edmund.setBirthday(datetime.date(1946, 2, 8))
gehard.setBirthday(datetime.date(1952, 6, 25))
angela.setBirthday(datetime.date(1950, 9, 17))
teresa.setBirthday(datetime.date(1958, 3, 9))
martin.setBirthday(datetime.date(1412, 4, 12))
siegfried.setBirthday(datetime.date(1960, 3, 25))
haagen.setBirthday(datetime.date(1962, 2, 18))
boris.setBirthday(datetime.date(1962, 7, 11))
Francis.setBirthday(datetime.date(1142, 2, 16))

print (friedrich.getName())
print (siegfried.getLastName())
print (ursala.getAge())

print(friedrich.__lt__(martin))
print(friedrich.__str__())
