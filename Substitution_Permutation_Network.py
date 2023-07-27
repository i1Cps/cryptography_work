import numpy as np

class SPN():
    def __init__(self, number_of_rounds=4, debug=False) -> None:
        self.number_of_rounds = number_of_rounds
        self.plain_text = None
        self.cipher_text = None
        self.key = None
        self.S_Box = None
        self.permutation = None
        self.round_keys = None
        self.debug = debug
        self.S_Box = {'0':'4', '1':'1', '2':'E', '3':'8',
                      '4':'D', '5':'6', '6':'2', '7':'B',
                      '8':'F', '9':'C', 'A':'9', 'B':'7',
                      'C':'3', 'D':'A', 'E':'5', 'F':'0'}
        
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
            msg = 'The maximum rounds of encryption is 13, you asked for ' + number_of_keys + ' rounds'
        # Calculate the minimum key length for given number of rounds
        
        
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
                print(i,': ',array_of_round_keys[i])

        return array_of_round_keys
    
    # XOR bitwise OP
    def XOR(self, state, round_key):
        # Check if state and round_key are the same length
        if len(str(state)) != len(str(round_key)):
            raise ValueError("current state and round key are different lengths")
        # XOR ~ Convert to binary datatype and pad to 16 bits
        xor = self.pad_bits(bin(int(state,2) ^ int(round_key,2)),16)
        return xor
        
    # Function to a=pad a bit_string to specified length
    def pad_bits(self, input, padded_length):
        # Takes binary string representation as input
        if len(input)-2 < padded_length:
            required_zeros = padded_length - (len(input)-2)
            return '0b' + '0' * required_zeros + input[2:]
        else:
            return input
        
    # Applies substitution box to current input state
    def apply_S_Box(self,input):
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
            substitution = self.S_Box[hexadecimal_value.upper()]
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
        
        self.plain_text = plain_text
        self.binary_plain_text = self.pad_bits(bin(int(self.plain_text,16)),16)
        self.key = self.pad_bits(bin(key),32)
        
        self.round_keys = self.get_round_keys(self.key, self.number_of_rounds + 1)
        
        state =self.binary_plain_text
        
        for i in range(self.number_of_rounds-1):
            if self.debug:
                print('Round number: ', i)
                print('state: ', state,)
                print('roundk:', bin(int(self.round_keys[i],2)))
            # XOR the state with the round key
            xor = self.XOR(state,self.round_keys[i])
            if self.debug: print('xor: ', xor)
            xor_sub = self.apply_S_Box(xor)
            if self.debug: print('xor_sub: ', xor_sub)
            xor_sub_perm = self.apply_P_Box(xor_sub)
            if self.debug: print('xor_sub_perm: ', xor_sub_perm)
            state = xor_sub_perm
            
        # XOR state with last round key and apply substitution box
        xor= self.pad_bits(bin(int(state,2) ^ int(self.round_keys[self.number_of_rounds-1],2)),16)
        xor_sub = self.apply_S_Box(xor)
        state = xor_sub
        self.binary_cipher_text = self.XOR(state, self.round_keys[self.number_of_rounds])
        self.cipher_text = format(int(self.binary_cipher_text,2),'x')
        
        print('Plain text in hexadecimal: ', self.plain_text,)
        print('Plain text in binary: ', self.binary_plain_text)
        print('Cipher text in hexadecimal: ', self.cipher_text)
        print('Cipher text in binary: ', self.binary_cipher_text)

# Create SPN 
substitution_permutation_network = SPN(debug=False)
# Enter plain text below
plain_text='aaaa'  
# Change key below 
key = 0b11100111011001111001000000111101

# If you have a binary plain text instead enter below
binary_plain_text = None 
if binary_plain_text:
    plain_text = format(int(binary_plain_text,2),'x')

# Encrypt
try:
    substitution_permutation_network.encrypt(plain_text, key)
except ValueError as err:
    print(err) 
    