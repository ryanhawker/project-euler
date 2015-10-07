#! /usr/bin/python

######## Problem Four #######
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009=91*99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
#############################

#String reverser
def revString(x):
    new_string = ""
    tmp = x[0]
    for i in range(1,len(x)):
        new_string += x[-i]
    new_string += tmp
    return new_string

#Lets write a isPalindrome function
def isPalindrome(candidate):
    rev = revString(str(candidate))
    if rev == str(candidate):
        return True
    else:
        return False

#Start from 999 x 999 and go down? simplest brute force method?
high = 1
for i in reversed(range(100, 999)):
    for j in reversed(range(100, 999)):
        if isPalindrome(i*j) and i*j > high:
            high = i*j
            break
print high

