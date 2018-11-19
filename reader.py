
# coding: utf-8

# In[49]:


import re
import numpy as np
import operand as op
import opcodes as opcode



    

source_code=open("code.txt",'r')
branch_op=['BR','BEQ','BNE','BLO','BLS','BHI','BHS']
lines = source_code.readlines()

symbol_dict={}
symbol_add={}
flag=True
translated_code=[]
pc=0
for line in lines:
    if line.strip():
        #print(line)  
        l=line.replace(","," ")
        l=l.split()
        l[0]=l[0].replace("ï»¿","") # txt file starts with this 
        instruction_elements=[]
        i=0
        while(i < len(l)):
            if(l[i]==';'):
                break 
            instruction_elements.append(l[i])
            i+=1
        #print(instruction_elements)
        if(i==0):   #comment
            continue
            # zero operand
            
        operand=[]
        for j in range(len(instruction_elements)-1):
            operand.append(instruction_elements[j+1])
            
        operation_code=instruction_elements[0]
        try:
            instruction_code=opcode.Opcodes[operation_code]
        except:
            
            data='define'
            #print(operation_code)
            if(operation_code.lower() == data.lower()):
            #print(operand[0])
                symbol_dict[operand[0]]= -(pc+1)
            else:
                br=operation_code.replace(':','')
                symbol_dict[br]= -(pc+1)
                translated_code.append(pc)
                pc+=1
            continue
        
            
        if(i==2):
            #print(instruction_elements)
            if operation_code.upper() in branch_op : 
                symbol_add[pc]=operand[0]
                flag=False
                
        if(flag != False):
            for i in range(len(operand)):
                #print(operand[i])
                mode_code,register_code=op.GetOperandMode(operand[i])

                no_words=opcode.NoOfWords[mode_code]
                if(no_words>0):
                    symbol_add[pc+1]=operand[i]
                pc+=no_words
                instruction_code+=" "+register_code+" "+mode_code
                #print(mode_code)  
                #print(register_code) 
            #print(instruction_code)
        pc+=1
        translated_code.append(instruction_code)
        print(pc)
for i in range(len(translated_code)):
    print(i,translated_code[i])
print(symbol_add)
print(symbol_dict)
for key in symbol_add:
    print(key)
    label=symbol_add[key]
    value=symbol_dict[label]
    print(value)
    v=str(-value-key)
    print(v)
    translated_code[key]+=" "


        

