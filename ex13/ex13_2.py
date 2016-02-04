# -*- coding: utf-8 -*-
from sys import argv

# this takes in 2 arguments (other than the script name), a price, 
# and the percentage to be taken off the price
script, number, percentageToBeTaken = argv

# no error detection used for if a user puts in anything other than a number
num = float(number)
pTBK = float(percentageToBeTaken)
percOff = ( num / 100 ) * pTBK
ans = num - percOff

# the %.2f is to display the float to only 2 decimal places, for formatting.
# I need to learn a better way to display this, such as using an integer
# for cents instead, or the decimal var
print "You started with €%.2f, you want to take %.2f%s off. You are left with €%.2f." % (
    num, pTBK, '%', ans )
