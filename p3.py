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
        #Print statements for testing this function
        print "Please try a number greater than 1"
    else:
        '''
        Loop up to the square root of our number, as all composite (non-prime) numbers have a prime factor 
        less than the numbers square root. To see a proof go to proof wiki and search for "Composite Number has
        Prime Factor not Greater Than its Square Root.
        '''
        for potential_factor in arange(2, candidate**0.5):
            if candidate%potential_factor == 0:
                #print "This aint no prime! It has a factor: %d" % potential_factor
                return False

        #print "This seems to be a prime number!"
        return True


