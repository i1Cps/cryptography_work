import numpy as np

class SPN():
    def __init__(self, number_of_rounds=4, debug=False) -> None:
        self.number_of_rounds = number_of_rounds
        self.plain_text = None
        self.cipher_text = None
        self.key = None
        self.permutation = None
        self.round_keys = None
        self.debug = debug
        self.s_box = {'0':'4', '1':'1', '2':'E', '3':'8',
                      '4':'D', '5':'6', '6':'2', '7':'B',
                      '8':'F', '9':'C', 'A':'9', 'B':'7',
                      'C':'3', 'D':'A', 'E':'5', 'F':'0'}
        self.inverse_s_box = None
        
        self.P_box = {1:1, 2:5, 3:9, 4:13, 5:2, 6:6, 7:10, 8:14,
                      9:3, 10:7, 11:11, 12:15, 13:4, 14:8, 15:12, 16:16}

    # Function produces 16 bit round keys from prime key, takes binary representation ('0b') input
    def get_round_keys(self,prime_key, number_of_keys):
        #Removes '0b' tag from binary representation
        prime_key = prime_key[2:]
        if self.debug: print("input key: ", prime_key)
        if len(prime_key) < 32:
            msg = 'The key you providied is ' + str(len(str(prime_key))) + ' which is less than 32 bits!'
            raise ValueError(msg)
        if number_of_keys > 13:
            msg = 'The maximum number of round keys you can generate is 13, you asked for ' + number_of_keys + ' keys'        
        
        # Initialise Nr empty arrays
        array_of_round_keys = [0 for i in range(number_of_keys)]
        
        # concatenate input key to perform easy cyclic shifts on 4 bit blocks
        #  64 (32+32) bit prime key = max 13 blocks, meaning max rounds is 13
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
            for j in range(4):
                round_key += bit_blocks[i+j]
            array_of_round_keys[i] = '0b' + ''.join(round_key)
        
        if(self.debug):
            print("round keys: ")
            for i in range(number_of_keys):
                print(i+1,': ',array_of_round_keys[i])

        return array_of_round_keys
    
    # XOR bitwise OP
    def XOR(self, state, round_key):
        # Check if state and round_key are the same length
        if len(str(state)) != len(str(round_key)):
            raise ValueError("current state and round key are different lengths")
        # XOR ~ Convert to binary datatype and pad to 16 bits
        xor = self.pad_bits(bin(int(state,2) ^ int(round_key,2)),16)
        return xor
        
    # Function to pad a bit_string to specified length
    def pad_bits(self, input, padded_length):
        # Takes binary string representation as input
        if len(input)-2 < padded_length:
            required_zeros = padded_length - (len(input)-2)
            return '0b' + '0' * required_zeros + input[2:]
        else:
            return input
        
    # Applies substitution box to current input state
    def apply_S_Box(self,input, inverse=False):
        input = input[2:] # Remove '0b' tag from beginning of binary string representation
        # Check input is 16 bits long
        if len(input) != 16:
            msg = 'The input to the S Box should be 16 bits, instead its ' + str(len(str(input))) + '!'
            raise ValueError(msg)
        
        # Split the 16 bit input input 4 blocks of 4 bits        
        bit_blocks = np.zeros(4,dtype='U4')
        for i in range(4):
            bit_blocks[i] = input[i*4:((i*4)+4)]
        
        # Perform substitution
        for i, block, in enumerate(bit_blocks):
            # Convert bin -> hex
            binary_value = block
            decimal_value = int(binary_value,2) # binary -> decimal
            hexadecimal_value = format(decimal_value,'x') # decimal -> hexadecimal
            # Substitute
            if inverse == True:
                substitution = self.inverse_s_box[hexadecimal_value.upper()]
            else:
                substitution = self.s_box[hexadecimal_value.upper()]
            # Convert hex -> bin
            decimal_value = int(substitution,16) # hexadecimal -> decimal
            binary_value = format(decimal_value,'04b') # decimal -> binary
            bit_blocks[i] = binary_value
        final_output = '0b'+''.join(bit_blocks)
        return final_output
    
    # Applies permutation box to input state
    def apply_P_Box(self,input):
        input = input[2:] # Remove '0b' tag from beginning of binary string representation
        # Check input is 16 bits long
        if len(input) != 16:
            msg = 'The input to the permutation box should be 16 bits, instead its ' + str(len(str(input))) + '!'
            raise ValueError(msg)
        # Split bit string into list of its bits
        bit_list = list(input)
        perumtated_bit_list = [0] *16
        for i, bit in enumerate(bit_list):
            # Adjust for correct permutation box index
            perumtated_bit_list[i] = bit_list[self.P_box[i+1] - 1]
            
        final_output = '0b'+''.join(perumtated_bit_list)
        return final_output        
        
    # PlainText 16 bits
    def encrypt(self, plain_text, key):
        print(key)
        self.plain_text = self.pad_bits(bin(plain_text),16)
        self.key = self.pad_bits(bin(key),32)
        
        self.round_keys = self.get_round_keys(self.key, self.number_of_rounds + 1)
        
        state = self.plain_text
        
        for i in range(self.number_of_rounds-1):
            if self.debug:
                print('Round number: ', i+1)
                print('state:       ', state,)
                print('roundk:      ', self.pad_bits(bin(int(self.round_keys[i],2)),16))
            # XOR the state with the round key
            xor = self.XOR(state,self.round_keys[i])
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
        
    def decrypt(self, cipher_text, key):
        self.cipher_text = self.pad_bits(bin(cipher_text),16)
        self.key = self.pad_bits(bin(key),32)
        state = self.cipher_text
        # Calculate inverse s box
        self.inverse_s_box = {value:key for key,value in self.s_box.items()}
        # Calculate the normal round keys
        self.round_keys = self.get_round_keys(self.key, self.number_of_rounds + 1)
        # Get round keys for decryption
        self.inverted_round_keys = self.round_keys[::-1]
        self.inverted_round_keys.append(self.round_keys[self.number_of_rounds])
        if self.debug:
            print('Round number: 1',)
            print('State:      ', state)
        xor = self.XOR(state,self.inverted_round_keys[0])
        if self.debug: print('xor:        ', xor)
        state = xor
        if self.debug:
            print('Round number: 2',)
            print('State:      ', state)
        inv_sub = self.apply_S_Box(state,inverse=True)
        if self.debug: print('inv_sub:    ', inv_sub)
        inv_sub_xor = self.XOR(inv_sub,self.inverted_round_keys[1])
        if self.debug: print('xor_inv_sub:',inv_sub_xor)
        state = inv_sub_xor
        
        for i in range(3,self.number_of_rounds +2):
            if self.debug:
                print('Round number: ', i)
                print('State:      ', state)
            perm = self.apply_P_Box(state)
            if self.debug: print('perm:       ', perm)
            perm_inv_s_box = self.apply_S_Box(perm, inverse=True)
            if self.debug: print('perm_inv:   ', perm_inv_s_box)
            perm_inv_s_box_xor = self.XOR(perm_inv_s_box,self.inverted_round_keys[i-1])
            if self.debug: print('perm_sxor:  ', perm_inv_s_box_xor)
            state = perm_inv_s_box_xor
            #round2 = self.XOR(self.apply_S_Box(round,inverse=True),self.inverted_round_keys[1])
            #print('State: ',self.XOR(round2,self.round_keys[self.number_of_rounds]))
        
        self.plain_text = state
        

# ------------------------------------------------------------------------

# Uncomment to run and use SPN file on its own

""" 
# Create SPN 
substitution_permutation_network = SPN(debug=True)
# Change key below 
key = 0b11100111011001111001000000111101
# Change plain text below
plain_text = 0b0100111010100001
# Change the cipher text below
cipher_text = 0b0111000011010100

# Encrypt
try:
    #substitution_permutation_network.encrypt(plain_text, key)
    substitution_permutation_network.encrypt(cipher_text, key)
except ValueError as err:
    print(err) 
     """