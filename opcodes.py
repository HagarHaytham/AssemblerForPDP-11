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
        'INC':'0001000000',#+00
        'DEC':'0001000100',
        'CLR':'0001001000',
        'INV':'0001001100',
        'LSR':'0001010000',
        'ROR':'0001010100',
        'RRC':'0001011000',
        'ASR':'0001011100',
        'LSL':'0001100000',
        'ROL':'0001100100',
        'RLC':'0001101000',
        
        #1 OP OFFSET
        'BR' :'0010000',
        'BEQ':'0010001',
        'BNE':'0010010',
        'BLO':'0010011',
        'BLS':'0010100',
        'BHI':'0010101',
        'BHS':'0010110',
        
        
        #0 OP INSTURCTION
        'HLT':'0000000000000000',#+000000000
        'NOP':'0000001000000000',
        # + 3 INSTRUCTIONS FROM JSR SUBROUTIINE INSTRUCRIONS
        'RTS':'0000010000000000',
        'INTERRUPT':'0000011000000000',
        'IRET':'0000100000000000',
        
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

    
