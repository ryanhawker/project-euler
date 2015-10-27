#! /usr/bin/python

####### PROBLEM THREE #######
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#############################
from pylab import *

#Start by writing an isPrime function to check if the factor is prime.
#Do it ourselves because it's a good thing to do.
def isPrime(candidate):
    if candidate <= 1:
        print "Please try a number greater than 1"
    else:
        '''
        Loop up to the square root of our number, as all composite (non-prime) numbers have a prime factor 
        less than the numbers square root. To see a proof go to proof wiki and search for "Composite Number has
        Prime Factor not Greater Than its Square Root.
        '''
        if candidate.is_integer():
            for potential_factor in arange(2, candidate**0.5):
                if candidate%potential_factor == 0:
                    return False
            return True
        else:
            return False 

under_test = 600851475143
list_comp = [z for z in arange(2, under_test**0.5) if under_test % z == 0] #List comprehension creates list of all the factors of under_test
#We then just loop through checking each factor for primeyness
for i in list_comp:
    if isPrime(i):
        print "i is a prime factor %d" % i



