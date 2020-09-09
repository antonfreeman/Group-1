#!/usr/bin/env python3
# Python Code Placeholder

class float:
	n = 0 		# the numerator of the number behind the dcm pnt
	d = 1		# the denominator of the number behind the dcm pnt
	c = 0 		# the characteristic of the number
	
	def set_c(self, value):
		self.c = value
	
	def set_n(self, value):
		self.n = value
	
	def set_d(self, value):
		self.d = value
		
	def get_c():
		return self.c
		
	def get_n():
		return self.n
	
	def get_d():
		return self.d

 
"""
    parse through string and remove 
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
	   
    return False    


"""
    parse through string and remove
    numbers behind decimal point from float
"""
def mantissa( num_string, float_obj ):
    
    # steps: again feel free to change this is rough
    # 1. parse string until "."
    # 2. grab index[1]
	# 3. convert decimal to fraction
    # 4. assign the result to external variables
	# 5. save numarator->float.n and denominator->float.d 
    # 6. Return success or failure flag

		# code here

    return False
    
def get_denominator( num_string ):
	
	# this should parse through the string and return a 10^x denominater
	return 10**0
 

