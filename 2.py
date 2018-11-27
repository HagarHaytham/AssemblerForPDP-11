# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 00:33:08 2018

@author: hagar
"""
#x = -14
#binint = int("{0:b}".format(x)) #convert to binary
#print (type(binint))
#print(binint)
##flipped = ~binint #flip the bits
##print(flipped)
##flipped += 1 #add one (two's complement method)
###intflipped=int(str(flipped),2) #faff about to get back to decimal (vanilla python doesn't like unsigned binints)
##print(flipped)
#def bin_add(*args): return bin(sum(int(x, 2) for x in args))[2:]
#def get_bin(x,n):
#    bits=format(abs(x), 'b').zfill(n)
#    
#    print(bits)
#    bits = list(bits)
#
#    if (x<0):
#        s=""
#        for i in range (len(bits)): # not 1's
#            if bits[i]=='0':
#                bits[i]='1'
#            else:
#                bits[i]='0'
#            s+=bits[i]
#        
#        
#        twoscomp = bin(int(s,2) + int('1',2))
#        st = str(twoscomp)
#        st=st[2:len(st)]
#        
#        print(s)
#        print("  str   "+st)
#        
#        #binint+=1
#        print(binint)
##        bits = abs(int("{0:b}".format(x)))
##        flipped = ~bits
###    print(bits)
###    flipped = ~bits
##    flipped += 1
##    print("f "+str(flipped))
#    
    


def get_bin(x,n):
    bits=format(abs(x), 'b').zfill(n)
    
    bits = list(bits)
    st=""
    if (x<0):
        s=""
        for i in range (len(bits)): # not 1's
            if bits[i]=='0':
                bits[i]='1'
            else:
                bits[i]='0'
            s+=bits[i]
        twoscomp = bin(int(s,2) + int('1',2))
        st = str(twoscomp)
        st=st[2:len(st)]
    else:
        for i in range (len(bits)):
            st+=bits[i]
    return st
st=""   
m=get_bin(2,9)
print(str(m))


#get_bin = lambda x, n: print(format(x, 'b').zfill(n))
#get_bin(x,9)
