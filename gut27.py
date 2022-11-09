#!/usr/bin/python3.8

def findPayment(loan, r, m):
# m = months
# r = rate
# loan = principle

    return loan * ((r*(1+r)**m) / ((1+r)**m - 1))

class Mortgage(object):
    def _init_(self, loan, annRate, months):

        self.loan = loan
        self.rate = annRate / 12
        self.months = months
        self.paid = [0.0]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None

# class Fixed(Mortgage)
#     def __init__(self, loan, r, months):
# 
#         Mortgage.__init__(self, loan, r, months)
#         self.legend = "Fixed, " +str(round(r*100), 2)) + "%"

# class FixedWithPts()
# class TwoRate()
principle = 20000
duration = 30
# in years

varMonths = 48
fixedRate = 0.07
pointsRate = 3.25
VarRate1 = 0.045
VarRate2 = 0.095
VarMths = 48

twoLakh = Mortgage()
twoLakh.__init__(self, principle, fixedRate, duration)
# print ("fixed rate = 7%", findPayment(principle, fixedRate, varMonths))
# print ("var rate 1 = 4.5%", findPayment(principle, VarRate1, varMonths))
# print ("var rate 2 = 9.5%", findPayment(principle, VarRate2, varMonths))


