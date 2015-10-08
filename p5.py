#! /usr/bin/python

####### Problem Five #######
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
############################

a = 2000 # Lets just start from 2000 for a laugh.
not_found = True

# Needs to be a multiple of 20, 19, 18, 17, 16, 14, 13, 11. These "contain" the numbers below 20 as factors.
factors = [20, 19, 18, 17, 16, 14, 13, 11]

while not_found:
    remainders = [a % f == 0 for f in factors]
    if all(remainders):
        print "We found the number: %d" % a
        not_found = False
    a += 20

#Please not that this is a very crappy solutions iwth not a lot of thought put into it :/
#I'll make it better some day. 
