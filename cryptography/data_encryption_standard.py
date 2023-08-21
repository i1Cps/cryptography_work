# DES The Feistel cipher
# Required functions:
#   Function to calculate round keys
#   Permutation function
#   Substitution function,
#   F function of DES which includes expansion function
#   main round function

import numpy as np
from helpers.binary_helper import BinaryHelper
#from cryptography.helpers.binary_helper import BinaryHelper

class DES():
    def __init__(self, debug=False) -> None:
        self.binary_helper = BinaryHelper()
        self.debug = debug
        self.number_of_rounds = 16
        self.prime_key = 0
        self.plain_text = 0
        self.cipher_text = 0
        self.permutation_box = [
            15,23,27,59,3,5,28,14,
            48,49,50,33,9,12,41,7,
            53,29,56,10,37,32,24,38,
            19,36,21,4,31,2,16,47,
            51,34,60,25,58,18,55,54,
            6,57,17,35,64,44,8,22,
            1,30,45,61,42,46,26,63,
            13,11,43,40,20,62,39,52
        ]
        # First and low columns are expanded indexs
        self.expansion_box = [
            32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9,10,11,12,13,
            12,13,14,15,16,17,
            16,17,18,19,20,21,
            20,21,22,23,24,25,
            24,25,26,27,28,29,
            28,29,30,31,31, 1
        ]
        
        # Takes a 48 bit input (8 6 bit blocks) and has a 32 bit output (8 4 bit blocks)
        # we treat the box as a table entry with x and y index keys
        # Bits 1 and 6 create the y index for each block 
        # Bits 2,3,4,5 create the x index for each block
        self.substitution_box = [
            14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7,
             0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8,
             4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0,
            15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13
        ]
    
    # Function produces 16 bit round keys from prime key, takes binary representation ('0b') input
    def get_round_keys(self, prime_key, number_of_keys):    
        #Removes '0b' tag from binary representation
        prime_key = prime_key[2:]
        if self.debug: print("input key: ", prime_key)
        if len(prime_key) < 56:
            msg = 'The key you providied is ' + str(len(str(prime_key))) + ' which is less than 56 bits!'
            raise ValueError(msg)
        if number_of_keys != 16:
            msg = 'The DES requires exactly 16 round keys, you ' + \
                'asked for ' + number_of_keys + ' keys'        
        
        # Initialise Nr empty arrays
        array_of_round_keys = [0 for i in range(number_of_keys)] 
        
        # concatenate input key to perform easy cyclic shifts
        prime_key = prime_key + prime_key
        
        # Split the concatonated prime key into blocks of 4 bits
        # Initialise      
        bit_blocks = np.zeros(int(len(prime_key)/4),dtype='U4')
        # Assignment
        for i in range(len(bit_blocks)):
            bit_blocks[i] = prime_key[i*4:((i*4)+4)]
                
        # Slice the round keys from concatenated prime key
        for i in range(number_of_keys):
            round_key = ''
            # 12 blocks of 4 bits creating 16 48 bit round keys
            for j in range(12):
                round_key += bit_blocks[i+j]
            array_of_round_keys[i] = '0b' + ''.join(round_key)
            
        if(self.debug):
            print("round keys: ")
            for i in range(number_of_keys):
                print(i+1,': ',array_of_round_keys[i])
                
        return array_of_round_keys

    def apply_permutation(self, input, initial_perm = False):
        input = input[2:] # Remove '0b' tag from beginning of binary string representation
        # Check input is 16 bits long
        if len(input) != 32 and not initial_perm:
            msg = 'The input to the permutation box should be 32 bits, ' + \
                'instead its ' + str(len(str(input))) + '!'
            raise ValueError(msg)
        if initial_perm and len(input) != 64:
            msg = 'The input to the permutation box should 64 for ' + \
                'initial permutation'
            raise ValueError(msg)
        
        # Split bit string into list of its bits
        output_len = 64 if initial_perm else 32
        bit_list = list(input)
        perumtated_bit_list = [0] * output_len
        for i, bit in enumerate(bit_list):
            # Adjust for correct permutation box index
            perumtated_bit_list[i] = bit_list[self.permutation_box[i] - 1]
            
        final_output = '0b'+''.join(perumtated_bit_list)
        print('final output p_box: ', final_output)
        return final_output        
            
    # Method to modify bits in binary number, index if right to left and starts at 1
    def modfidy_bit(self, bit_string, bit_index, new_bit):
        mask = 1 << bit_index # mask for the target bit
        masked_bit_string = bit_string & ~mask
        modified_bit_string = masked_bit_string | (new_bit << bit_index)
        return modified_bit_string
    
    def get_bit(self, bit_string, bit_index):
        shifted = bit_string << bit_index
        print(bin(bit_string))
        print(bin(shifted))
    
    def des_f_function(self,bit_block,round_key):
        bh= self.binary_helper
        # Expand bit block to 48 bits (32 -> 48) ( 8 blocks of 6 bits)
        expanded_bit_block = bh.expand_bit_block(bit_block,48)
        # XOR bit block with key
        # Apply substitution block - 6 bit sub blocks to 4 bit sub blocks ( 12 blocks of 4 bits)
        # Apply permutation block
        
        return True
    
    def feistal_structure(self, plain_text, round_keys, number_of_rounds):
        bh = self.binary_helper
        print(len(self.plain_text)/2)
        left_bit_block = plain_text[:len(plain_text)/2]
        right_bit_block = plain_text[len(plain_text):]
        for i in range(16):
            next_left_bit_block = right_bit_block
            adjusted_right_bit_block = self.des_f_function(right_bit_block, )
            next_right_bit_block = bh.XOR(left_bit_block, adjusted_right_bit_block)
            left_bit_block = next_left_bit_block
            right_bit_block = next_right_bit_block
            
            
            
        
    
    # INPUT: plaintext block (64 bits)
    def encrypt(self, plain_text, key):
        # Use binary helper functions
        bh = self.binary_helper
        # Rerepresent plainText as binary number
        self.plain_text = bh.pad_bits(bin(plain_text),64)
        self.key = bh.pad_bits(bin(key),56)
        if self.debug: print('Plain text: ', self.plain_text)
        self.round_keys = self.get_round_keys(self.key, self.number_of_rounds)
        
        # Apply initial permutation
        self.plain_text = self.apply_permutation(self.plain_text, initial_perm=True)
        
        print('IP plain text: ', self.plain_text)
        # Apply ronud functions
        self.plain_text = self.feistal_structure(self.plain_text, self.round_keys, 
                                                 self.number_of_rounds)
        
        
        state = self.plain_text
        return True
        for i in range(self.number_of_rounds-1):
            if self.debug:
                print('Round number: ', i+1)
                print('state:       ', state,)
                print('roundk:      ', self.pad_bits(bin(int(self.round_keys[i],2)),16))
            # XOR the state with the round key
            xor = bh.XOR(state,self.round_keys[i])
            if self.debug: print('xor:         ', xor)
            xor_sub = self.apply_S_Box(xor)
            if self.debug: print('xor_sub:     ', xor_sub)
            xor_sub_perm = self.apply_P_Box(xor_sub)
            if self.debug: print('xor_sub_perm:', xor_sub_perm)
            state = xor_sub_perm
            
        # XOR state with the second to last round key and apply substitution box
        xor= self.pad_bits(bin(int(state,2) ^ int(self.round_keys[self.number_of_rounds-1],2)),16)
        xor_sub = self.apply_S_Box(xor)
        state = xor_sub
        if self.debug:
            print('Round number: ', self.number_of_rounds)
            print('State:       ', state)
        # XOR with last round key
        self.cipher_text = self.XOR(state, self.round_keys[self.number_of_rounds])
        if self.debug:
            print('Round number: ', self.number_of_rounds+1)
            print('State:       ', self.cipher_text)
            print('-----------------------------')
            print('Plain text in binary:  ', self.plain_text)
            print('Cipher text in binary: ', self.cipher_text)
        
        # Apply initial permutation
        plainText = self.apply_permutation(plainText, self.initial_permutation_box)
    
        return True




# Create DES 
data_encryption_standard = DES(debug=True)
# Change key (56 bit) below 
key = 0b10101010101011001010101010110101010101010101010110100011
# Change plain text below (64 bit)
plain_text = 0b1001010000000001001000000000011010100000001100000000000000110110

# Change the cipher text below
cipher_text = 0b0111000011010100

# Encrypt
try:
    data_encryption_standard.encrypt(plain_text, key)
except ValueError as err:
    print(err) 
    