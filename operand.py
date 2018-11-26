# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:37:54 2018

@author: hagar
"""

import opcodes as op
import re
def GetOperandMode(operand):
    #this should return 1- addressing mode 2- the register number
    mode=""
    reg=""
    indirect=""
    
    if (operand[0]=='@'):
        indirect="indirect"
        operand=operand.replace(operand[0],"")
    
        
    #PC addressing modes
    #1- immediate (autoincrement)    #100
    #2- absolute (autoincrementindirect) @#100      
    #3- relative (index)  varible A
    #4- relative indirect (indexindirect) @variable @A
    if '#' in operand:
        operand="(R7)+"
    elif re.search('[R][0-7]', operand) == None: 
        #this means this is a variable
        operand="X(R7)" # indexed
    

    # replace letters of a var before (  with X  
    # to handel var(R0) index mode
    if ("(" in operand and operand[0]!='-') :
        if operand[0] != "(":
           operand=operand.replace(operand[0],"X")
           while (operand[1] != "(" ):
               operand = list(operand)  # Convert the string to a list
               operand[1] = ""  # Change the character using its index 
               operand = "".join(operand)  # Change the list back to string, by using 'join' method of strings
 
            #this one doesn't work as if the variable name contains r for example it will remove the r letter of the register
            #operand=operand.replace(operand[1],"") #this one doesn't work

    
    
    
    out="" 
    if '+' in operand:
        mode ="autoincrement"
        out='+'
    elif '-' in operand:
        mode ="autodecrement"
        out='-'
    elif 'X' in operand:
        mode ="index"
        out='X'
    elif re.search('[R][0-7]', operand) != None: 
        mode ="register"
    operand=operand.replace(out,"")
    operand=operand.replace('(',"")
    operand=operand.replace(')',"")
#    print(operand)
    

    
    mode += indirect
    reg = operand
    #print (mode)
    #print (reg)
    modeCode=op.AddressingModes[mode]
    regCode=op.Register[reg]
    return modeCode,regCode



m,r=GetOperandMode("(R5)")
print (m)
print (r)
