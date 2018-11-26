# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 00:33:08 2018

@author: hagar
"""

x = -14
binint = int("{0:b}".format(x)) #convert to binary
print(binint)
flipped = ~binint #flip the bits
print(flipped)
flipped += 1 #add one (two's complement method)
#intflipped=int(str(flipped),2) #faff about to get back to decimal (vanilla python doesn't like unsigned binints)
print(flipped)

get_bin = lambda x, n: print(format(x, 'b').zfill(n))
get_bin(x,9)