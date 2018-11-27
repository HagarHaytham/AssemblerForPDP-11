

import re
import operand as op
import opcodes as opcode


def place_symbols(symbol_add,symbol_dict,translated_code,labels):
    for key in symbol_add:  
        label=symbol_add[key]
        bits=0
        if(label in labels):
            print(label,"label")
            bits=9
        else:
            print(label,"variable")
            bits=16
        #print(key,label)
        value=symbol_dict[label]
        offset=-value-key-1
        offset=get_bin(offset,bits)###########################################
        translated_code[key]+=str(offset)
        #translated_code[key]+=" "+bin(v & 0b1111111111111111)
        translated_code[key]+=str(offset)

def get_bin(x,n): # get binary of an offset 
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
    

def place_immediate_values(indexed_hashed,translated_code):
    for key in indexed_hashed:
        #print(key)
        v=indexed_hashed[key]
        #translated_code[key]=bin(int(v) & 0b1111111111111111)
        #translated_code[key]=bin(int(v) & 0b1111111111111111)
        translated_code[key]=v
def place_indexed_variables(variable_add,symbol_dict,translated_code):
    for key in variable_add:  
         print(key)
         variable=variable_add[key]
         address=-symbol_dict[variable]
         translated_code[key]+=str(address)      
         
def place_subroutines_add(subroutine_add,subroutine_dict,translated_code):
      for key in subroutine_add:  
        label=subroutine_add[key]
        #print(key,label)
        value=subroutine_dict[label]
        #translated_code[key]+=" "+bin(v & 0b1111111111111111)
        translated_code[key]+=str(value)



def assembler():
    source_code=open("code.txt",'r')
    lines = source_code.readlines()
    label=':'
    pc_modes='[@]*[#]+[0-9]+'
    indexed='[@]*[0-9]+[(][[R][0-7][)]+'
    auto_indirect='[-]*[(][[R][0-7][)]+[+]*'
    data='define'
    branch='[B]+[A-Z]*[A-Z]*'
    indirect='[(]+[R]+[0-7]+[)]+'
    indexed_indirect='([@]+[A-Z]*)\w+'
    labels=[]
    subroutine='jsr'
    subroutine_flag=False
    symbol_dict={}
    symbol_add={}
    variable_add={}
    indexed_hashed={}
    subroutine_dict={}
    subroutine_add={}
    translated_code=[]
    pc=0
    for line in lines:
        if line.strip():
            flag=True
            prev_pc=pc
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

            op_start=1
            op_end=len(instruction_elements)
            operation_code=instruction_elements[0]  
            if re.search(label,operation_code ) != None :
                operation_code=operation_code.replace(':',"")
                if(subroutine_flag == False):
                    symbol_dict[operation_code]=-(pc)
                else:
                    subroutine_dict[operation_code]=(pc)
                    subroutine_flag=False
                if(len(instruction_elements) == 1):
                    continue
                else: 
                     operation_code=instruction_elements[1]
                     op_start+=1
            if re.search('subroutine',operation_code.lower()) != None :
                subroutine_flag=True
                continue
            
            operand=[]
            for j in range(op_start,op_end):
                operand.append(instruction_elements[j])

            if (data == operation_code.lower()):
                symbol_dict[operand[0]]=-(pc)
                pc+=1     
                continue
            try:   
                instruction_code=opcode.Opcodes[operation_code.upper()]   
            except:
                print("instruction "+operation_code+" not found !!")
                return
            if re.search(branch,operation_code, re.IGNORECASE) != None :
                symbol_add[pc]=operand[0]
                labels.append(operand[0])
                flag=False 
            if re.search(subroutine,operation_code, re.IGNORECASE) != None :
                print(pc)
                pc+=1
                subroutine_add[pc]=operand[0]
                flag=False 
            pc+=1  
            updated_pc=pc
            dist=0
            no_words=0
            if(flag != False):
                for i in range(len(operand)):
                    mode_code,register_code=op.GetOperandMode(operand[i])
                    no=opcode.NoOfWords[mode_code]
                    no_words+=no
                    if no>0:  
                        updated_pc+=1
                        if re.search(pc_modes,operand[i], re.IGNORECASE) != None :
                            oper=operand[i].replace("#","")
                            oper=oper.replace("@","")
                            indexed_hashed[pc+dist]=oper
                            dist+=1
                        elif re.search(indexed,operand[i], re.IGNORECASE) != None :
                            oper=operand[i].replace("@","")
                            oper=re.sub(indirect,"",oper,flags=re.IGNORECASE)
                            indexed_hashed[pc+dist]=oper
                            dist+=1
                        elif(re.search(indexed_indirect,operand[i], re.IGNORECASE) != None  ):
                            oper=operand[i].replace("@","")  
                            variable_add[pc+dist]=oper
                            dist+=1
                        elif(re.search(auto_indirect,operand[i], re.IGNORECASE) == None  ):  
                            symbol_add[pc+dist]=operand[i]
                            dist+=1      
                    instruction_code+=register_code+mode_code
            pc+=no_words     
            for i in range (pc-prev_pc):
                translated_code.append(instruction_code)
                instruction_code=""


    place_symbols(symbol_add,symbol_dict,translated_code,labels)
    place_immediate_values(indexed_hashed,translated_code)
    place_indexed_variables(variable_add,symbol_dict,translated_code)
    place_subroutines_add(subroutine_add,subroutine_dict,translated_code)
    f = open("Assembled_code.txt", "w")
    for i in range(len(translated_code)):
        print(i,translated_code[i]) 
        f.write(str(i)+"  "+str(translated_code[i])+'\n')
    f.close()    
        
assembler()
