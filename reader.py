
# coding: utf-8

# In[99]:


import re
import numpy as np
import operand as op
import opcodes as opcode
source_code=open("code.txt",'r')
lines = source_code.readlines()
label=':'
immediate='[#]+[0-9]+'
indexed='[@]*[0-9]+[(][[R][0-7][)]+'
indirect='[-]*[(][[R][0-7][)]+[+]*'
data='define'
branch='[B]+[A-Z]*[A-Z]*'
indirect='[(][[R][0-7][)]+'
symbol_dict={}
symbol_add={}
indexed_hashed={}
translated_code=[]
pc=0
for line in lines:
    if line.strip():
        flag=True
        prev_pc=pc
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
        
        if(i==0):   #comment 
            continue
        
        
        operation_code=instruction_elements[0]  
        if re.search(label,operation_code) != None:
            operation_code=operation_code.replace(':',"")
            symbol_dict[operation_code]=-(pc)
            continue
        operand=[]
        for j in range(len(instruction_elements)-1):
            operand.append(instruction_elements[j+1])
            
            if re.search(immediate,operand[j]) != None :
                oper=operand[j].replace("#","")
                indexed_hashed[pc+1]=oper
                
            if re.search(indexed,operand[j]) != None :
                oper=operand[j].replace("@","")
                re.sub(indirect,"",oper)
                indexed_hashed[pc+1]=oper
        
        if (data == operation_code.lower()):
            symbol_dict[operand[0]]=-(pc+1)
            pc+=1
           
            continue
        
        instruction_code=opcode.Opcodes[operation_code]    
        
        
        if re.search(branch,operation_code) != None :
            symbol_add[pc]=operand[0]
            flag=False     
        
        if(flag != False):
            for i in range(len(operand)):
                
                mode_code,register_code=op.GetOperandMode(operand[i])
                no_words=opcode.NoOfWords[mode_code]
                
                if no_words>0:
                    if(re.search(indirect,operand[i]) == None and re.search(indexed,operand[i]) ==None and re.search(immediate,operand[i]) ==None):
                        symbol_add[pc+1]=operand[i]
                pc+=no_words
                instruction_code+=" "+register_code+" "+mode_code
                
        pc+=1 
        for i in range (pc-prev_pc):
            translated_code.append(instruction_code)
            instruction_code=""
for key in symbol_add:  
    label=symbol_add[key]
    value=symbol_dict[label]
    v=value+key
    translated_code[key]+=" "+bin(v & 0b1111111111111111)
print(indexed_hashed)
for key in indexed_hashed:
    v=indexed_hashed[key]
    print(key,v)
    translated_code[key]=bin(int(v) & 0b1111111111111111)
print(translated_code)    

        

