
class BinaryHelper():
    def __init__ (self):
        self.exist=True
    
    # Takes a string variable (binary representaion are just strings)        
    def is_binary_number(self,input):
        if type(input)  == str:
            # for each char in string check if its a 0 or a 1
            for char in input:
                if char == '1' or char  == '0':
                    continue
                else:
                    return False
            return True
                    
        
        
    