#!/usr/bin/env python3

class float:
    def __init__(self):
        _n = 0 		# the numerator of the number behind the dcm pnt
        _d = 1		# the denominator of the number behind the dcm pnt
        _c = 0 		# the characteristic of the number

    def set_c(self, value):
        self._c = value
        
    def set_n(self, value):
        self._n = value

    def set_d(self, value):
        self._d = value

    def get_c(self):
        return self._c

    def get_n(self):
        return self._n

    def get_d(self):
        return self._d
    
    def __str__(self):
        opp_char = " + ( "
        
        if self.get_c() < 0 :
            opp_char = " - ( "
            
        if self.get_n() != 0:
            return str(self.get_c()) + opp_char + str(self.get_n()) + \
                   " / " + str(self.get_d()) + " )"
        else:
            return str(self.get_c()) + " + 0"
    

    
"""
parse through string or char list and remove 
whole integer from float                                 
"""
def characteristic( num_string, float_obj ):

    # steps: feel free to change this is rough
    # 1. split string on "."
    # 2. grab string from first index after split
    # 3. filter out any extra characters 
    # 4. cast to int (note: int WILL parse +/- symbols)
    # 5. assign the result to float.c
    # 6. Return success or failure flag

        # code here
    number = int( sanitize(num_string).split(".")[0] )
    float_obj.set_c( number )
    
    return float_obj.get_c() == int(number)


"""
parse through string or char list and remove
numbers behind decimal point from float
"""
def mantissa( num_string, float_obj ):
    
    # steps: again feel free to change this is rough
    # 1. split string on "."
    # 2. grab index[1]
    # 3. convert decimal to fraction
    # 4. assign the result to external variables
    # 5. save numarator->float.n and denominator->float.d 
    # 6. Return success or failure flag

        # code here
    number = sanitize(num_string).split(".")[1]
    float_obj.set_n( int(number) )
    float_obj.set_d( get_denominator(number) )
    
    return float_obj.get_n() == int(number) and \
    	   float_obj.get_d() == get_denominator(number)

    
def get_denominator( num_string ):
    # this should parse through the string and return a 10^x denominater
    return 10**len(num_string)
    
    
def sanitize(num_string):
    # removes all characters from num_string
    # except +, -, '.', and numbers 0-9 
    if num_string.count('.') > 1 or \
       num_string.count('-') > 1 or \
       num_string.count('+') > 1:
         return "0.0"
    num_string = num_string.strip("\0")
    new_num = '0'
    
    for i in num_string:
        i = ord(i)
        
        if (i < ord('9')+1 and i > ord('0')-1) or i == ord('.') or \
           i == ord('+') or i == ord('-'):
            new_num += chr(i)
            
    # check to see if string_num has no decimal point 
    # if it passes add a decmal point and 0's to end
    if "." not in new_num:
        new_num += ".00"
    
    
    return new_num

def main():
    test = input()#"123.456")                    # test value
    test_float = float()                # container for result
    
    characteristic(test, test_float)    # get and store characteristic in test_float
    mantissa(test, test_float)          # get and store mantissa in test_float
    
    print(test_float)
    
main()
    
    
    
