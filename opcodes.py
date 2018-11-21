# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:10:17 2018

@author: hagar
"""
# you give it the operation and it returns the binary code of it
Opcodes = {
        #2 OP INSTRUCTION
        'MOV':'0111',
        'ADD':'1000',
        'ADC':'1001',
        'SUB':'1010',
        'SBC':'1011',
        'AND':'1100',
        'OR' :'1101',
        'XNOR':'1110',
        'CMP':'1111',
        
        #1 OP DISTNATION
        'INC':'00010000',
        'DEC':'00010001',
        'CLR':'00010010',
        'INV':'00010011',
        'LSR':'00010100',
        'ROR':'00010101',
        'RRC':'00010110',
        'ASR':'00010111',
        'LSL':'00011000',
        'ROL':'00011001',
        'RLC':'00011010',
        
        #1 OP OFFSET
        'BR' :'0010000',
        'BEQ':'0010001',
        'BNE':'0010010',
        'BLO':'0010011',
        'BLS':'0010100',
        'BHI':'0010101',
        'BHS':'0010110',
        
        
        #0 OP INSTURCTION
        'HLT':'0000000',
        'NOP':'0000001',
        # + 3 INSTRUCTIONS FROM JSR SUBROUTIINE INSTRUCRIONS
        'RTS':'0000010',
        'INTERRUPT':'0000011',
        'IRET':'0000100',
        
        #JSR INSTRUCTION
        'JSR':'0011000000000000' # 0011 + something
        
        }


#you give it the addressing mode and it returns the binary code of it
AddressingModes={
        'register':'000',
        'registerindirect':'001',
        'autoincrement':'010',
        'autoincrementindirect':'011',
        'autodecrement':'100',
        'autodecrementindirect':'101',
        'index':'110',
        'indexindirect':'111'
        
        }

# you give it the binary code of addressing mode and it returns the number of words
NoOfWords={ # 7d yt check 3la dah !!!!!!
        '000':0,
        '001':0, 
        '010':1,
        '011':1,
        '100':0,
        '101':0,
        '110':1,
        '111':1
        }


Register={
        'R0':'000',
        'R1':'001', 
        'R2':'010',
        'R3':'011',
        'R4':'100',
        'R5':'101',
        'R6':'110',
        'R7':'111'
        
        }

    
