# DES The Feistel cipher
# Required functions:
#   Function to calculate round keys
#   Permutation function
#   Substitution function,
#   F function of DES which includes expansion function
#   main round function

import numpy as np


class DES_Feistel_Block_Cipher():
    def __init__(self, key) -> None:
        self.prime_key = key
        self.initial_permutation_box = [
            15,23,27,59,3,5,28,14,
            48,49,50,33,9,12,41,7,
            53,29,56,10,37,32,24,38,
            19,36,21,4,31,2,16,47,
            51,34,60,25,58,18,55,54,
            6,57,17,35,64,44,8,22,
            1,30,45,61,42,46,26,63,
            13,11,43,40,20,62,39,52
        ]
    
    # INPUT: plaintext block (64 bits)
    def encrypt(self, plainText):
        # Rerepresent plainText as binary number
        plainText = bin(plainText)
        print('gasdg',plainText)
        
        # Call function to calculate round keys
        try:
            round_keys =self.get_round_keys(key)
        except ValueError as err:
            print(err) 
        
        # Apply initial permutation
        plainText = self.apply_permutation(plainText, self.initial_permutation_box)
    
        return True
    
    def get_round_keys(self, prime_key):    
        # Converts back to binary representation
        prime_key = bin(prime_key)[2:]
        print("input key: ")
        print(prime_key)
        if len(prime_key) != 56:
            msg = 'The key you providied is ' + str(len(str(prime_key))) + ' bits not 56 bits!'
            raise ValueError(msg)
        
        # Initialise 16 empty arrays
        array_of_round_keys = []
        array_of_round_keys = [0 for i in range(16)] 
        
        # concatenate input key to perform easy cyclic shifts
        prime_key = prime_key + prime_key
        
        # Slice the round keys from concatenated prime key
        prime_key = str(prime_key)
        for round_key in range(16):
            array_of_round_keys[round_key] = prime_key[round_key:47+round_key]
            
        print("round keys: ")
        for i in range(16):
            print(array_of_round_keys[i])

        return array_of_round_keys

    def apply_permutation(self, input, permutation_box):
        input = input[2:]
        print('input',input)
        # deep copy sort of
        fixed_input = input[:]
        output = np.zeros(64)
        
        for bit in range(len(input[2:])):
            perm_index = permutation_box[bit]
            # Get the bit at index 15
            new_bit = self.get_bit(input,perm_index)
            
            print('hh',perm_index)
            #fixed_input = self.modfidy_bit(input,permutation_box[bit],0)
            #print(fixed_input[int(permutation_box[bit])-1])
            print(bit)
            #output[bit] = fixed_input[int(permutation_box[bit])-1]
            
            #print('done')
            
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


# 56 bit
key = 0b10101010101011001010101010110101010101010101010110100011
print(bin(key))
shifted = key >> 2
final = shifted << 2
print(bin(shifted))
print(bin(final))
string = '0b100100'
# 64 bit
plain_text = 0b1001010000000001001000000000011010100000001100000000000000110110

DES = DES_Feistel_Block_Cipher(key)
print('modi',bin(DES.modfidy_bit(key,1, 0)))
DES.encrypt(plain_text)
