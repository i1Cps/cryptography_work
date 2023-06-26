# DES The Feistel cipher
# Required functions:
#   Function to calculate round keys
#   Permutation function
#   Substitution function,
#   F function of DES which includes expansion function
#   main round function

def get_round_keys(input_key):    
    # Example Input: 10101010101011001010101010110101010101010101010110100011
    # Example output: array_of_round_keys

    # Check length of input_key
    if len(str(input_key)) != 56:
        return False
    
    array_of_round_keys = []
    array_of_round_keys = [0 for i in range(16)] 
    
    # concatenate input key to perform easy cyclic shifts
    input_key = int(str(input_key) + str(input_key))
    
    # Slice the round keys from concatenated input key
    input_key = str(input_key)
    for round_key in range(16):
        array_of_round_keys[round_key] = input_key[round_key:47+round_key]
        
    print("input key: ",input_key)
    print("round keys: ")
    for i in range(16):
        print(array_of_round_keys[i])

    return array_of_round_keys

def apply_permutation(input, permutation_box):
    input = str(input)
    fixed_input = input[:]
    output = []
    
    
    for bit in range(len(input)):
        output[bit] = fixed_input[int(permutation_box[bit])-1]

initial_permutation_box = [15,23,27,59,3,5,28,14,
                           48,49,50,33,9,12,41,7,
                           53,29,56,10,37,32,24,38,
                           19,36,21,4,31,2,16,47,
                           51,34,60,25,58,18,55,54,
                           6,57,17,35,64,44,8,22,
                           1,30,45,61,42,46,26,63,
                           13,11,43,40,20,62,39,52]

# INPUT: plaintext block (64 bits) and key (56 bits)
def DES(plainText, key):
    
    # Call function to calculate round keys
    round_keys = get_round_keys(key)
    if round_keys == False:
        print("print('Error - input key is wrong length')")
    
    # Apply initial permutation
    plainText = apply_permutation(plainText, initial_permutation_box)
    
    
    return True

# 56 bit
key = 0b10101010101011001010101010110101010101010101010110100011
# 64 bit
plain_text = int(0b0001010000000001001000000000011010100000001100000000000000110110)

DES(plain_text, key)

