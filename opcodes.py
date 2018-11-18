# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:10:17 2018

@author: hagar
"""

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