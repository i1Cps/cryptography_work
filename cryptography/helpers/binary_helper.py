
class BinaryHelper():
    def __init__ (self):
        self.exist=True
    
    # Takes a string variable (binary representaion are just strings)        
    def is_binary_number(self,input):
        if type(input)  == str:
            # For each char in string check if its a 0 or a 1
            for char in input:
                if char == '1' or char  == '0':
                    continue
                else:
                    return False
            return True
    
    # XOR bitwise OP (This takens binary representation E.G. 0b101....)
    def XOR(self, input1, input2, pad_bit_to = 16):
        # Check if state and round_key are the same length
        if len(str(input1)) != len(str(input2)):
            raise ValueError("XOR: input1 and input2 are different lengthss")
        # XOR ~ Convert to binary datatype and pad to 16 bits
        xor = self.pad_bits(bin(int(input1,2) ^ int(input2,2)),len(input1)-2)
        return xor
    
    # Function to pad a bit_string to specified length
    def pad_bits(self, input, padded_length):
        # Takes binary string representation as input
        if len(input)-2 < padded_length:
            required_zeros = padded_length - (len(input)-2)
            return '0b' + '0' * required_zeros + input[2:]
        else:
            return input       
    
    
        
        
    