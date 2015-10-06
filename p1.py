#! /usr/bin/python

#### Problem One #####
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.
######################
target = 1000

#Basic, slow for-loop version. Very slow if you change from below 1,000 to below 1,000,000!
tot = 0
for val in range(1, target):
    if val%3==0: tot += val
    elif val%5==0: tot += val
print "Slow and simple solution: %d" % tot


#Smarter solution is to calculate the sum of numbers less than 1000 that are divisible by 3, 
#add that to the sum of numbers less than 1000 that are divisible by 5 and then subtract
#the numbers less than 1000 that are divisible by 15 (or they'll get counted twice)
def SumDivBy(x):
    p = (target-1) / x
    return x * (p*(p + 1)) / 2

tot = SumDivBy(3)+SumDivBy(5)-SumDivBy(15)
print "More robust and efficient solution: %d" % tot
