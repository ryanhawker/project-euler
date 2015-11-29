#! /usr/bin/python

####### Problem Six #######
#
#   Find the difference between the sum of squares and the square of the sum up to 100
#
############################

# The sum of all numbers squared up to some MaxNum is given by:
max_num = 100
sum_squared = (max_num*(max_num/2) + (max_num/2))**2

# The square of the sum of all numbers up to MaxNum is given by:
square_sum = max_num*(max_num+1)*(2*max_num+1)/6

diff = sum_squared - square_sum 
print diff

# Do some googling for the proofs of the above equationns. They're pretty fun.
