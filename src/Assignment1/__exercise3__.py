'''
#===============================================================================
# Source Coding and Data Compression
# Assignment #1
#===============================================================================

Exercise 3: Use Matlab or other language to implement the encoding and decoding. If 
needed, make necessary assumptions. 

Created on Sep 25, 2014

@author: Liu Cheng
@version: 2.0
'''

LETTERS = ["1", "2" , "3"]
PROBABILITIES = [0.8, 0.02, 0.18]
MODEL = [LETTERS, PROBABILITIES]
SEQUENCE_1 = ["1", "3", "2", "1"]
SEQUENCE_2 = ["3", "2", "1", "1"]

#------------------------------------------------------------------------------ Encode Class
class Tag_Encode(object):
    '''Generation of arithmetic encode for given sequence'''
    # initialize lower bound and upper bound with 0 and 1
    lower_bound = 0
    upper_bound = 1
    # Fx(0) is assigned to 0 in very beginning
    fx = []
    # variable temp will be used in temporary storage
    temp = 0
    # output is the encode sequence, which is initialized as blank list
    output = []

    def __init__(self, model, sequence):
        '''Initialize letters and probabilities with model (comprise of such two lists)'''
        self.letters = model[0]
        self.probabilities = model[1]
        self.sequence = sequence
        self.fx_generation()
        self.encode_sequence_generate(self.sequence)
        
    def fx_generation(self):
        '''Calculate the Fx(1), Fx(2), Fx(3), etc. Store these values in fx[]'''
        for i in self.probabilities:
            temp = self.temp
            self.temp += i
            # get a list with 3 items, each item is made of lower Fx and upper Fx
            self.fx.append([temp, self.temp])
        
    def encode_sequence_generate(self, sequence):
        '''Generate encode sequence with bounds updating and scale methods'''
        for i in sequence:
            bounds = self.fx[self.letters.index(i)]
            # decide lower Fx and upper Fx which depends on the letter
            lower_fx, upper_fx = bounds[0], bounds[1]
            self.update_bounds(lower_fx, upper_fx, self.lower_bound, self.upper_bound)
            while (self.upper_bound < 0.5 or self.lower_bound >= 0.5):
                # in such conditions, choice proper scale and add 0 or 1 to output
                if self.upper_bound < 0.5:
                    self.e1_scale()
                    self.output.append("0")
                elif self.lower_bound >= 0.5:
                    self.e2_scale()
                    self.output.append("1")
        # add 100000 as the end of output
        self.output.append("100000")
            
    def update_bounds(self, lower_fx, upper_fx, lower_bound, upper_bound):
        '''Update bounds as soon as a new letter comes'''
        self.lower_bound = lower_bound + (upper_bound - lower_bound) * lower_fx
        self.upper_bound = lower_bound + (upper_bound - lower_bound) * upper_fx
        
    def e1_scale(self):
        '''Realize E1 scale method'''
        self.lower_bound *= 2
        self.upper_bound *= 2
        
    def e2_scale(self):
        '''Realize E2 scale method'''
        self.lower_bound = 2 * (self.lower_bound - 0.5)
        self.upper_bound = 2 * (self.upper_bound - 0.5)
        
    def get_output(self):
        return self.output

    def clear(self):
        '''Clear all variables in Class'''   
        self.fx = []
        self.temp = 0
        self.output = []
        self.lower_bound = 0
        self.upper_bound = 1
        self.model = {}
        self.sequence = []
        
#------------------------------------------------------------------------------ Decode Class
class Tag_Decode(object):
    '''Decode given sequence with model'''
    buffer = 0
    lower_bound = 0
    upper_bound = 1
    temp = 0
    fx = []
    output = []
    flag = True
    # store the indices of sequence
    index_sequence = 0
    
    def __init__(self, model, sequence):
        '''Initialize letters and probabilities with model (comprise of such two lists)'''
        self.letters = model[0]
        self.probabilities = model[1]
        self.sequence = sequence
        self.fx_generation()
        self.decode_sequence_generate(self.index_sequence)
        
    def decode_sequence_generate(self, index_sequence):
        '''Generate decode sequence with rescale methods'''
        i = self.index_sequence
        # make a lifelong loop until return occurs
        while True:
            if self.upper_bound >= 0.5 and self.lower_bound < 0.5:
                # choose specific length of sequence for further process
                temp_sequence = self.sequence[i:i+6] 
                if self.flag == True:
                    self.temp = self.calc_values(temp_sequence)                  
                    self.flag = False
                # get temp value with respect to lower bound and upper bound
                self.temp = (self.temp - self.lower_bound) / (self.upper_bound - self.lower_bound) 
                # update fx and get add letter to output value             
                lower_fx, upper_fx = self.search_fx()
                # update bounds value which is similar to encode class
                self.update_bounds(lower_fx, upper_fx, self.lower_bound, self.upper_bound)    
                # loop will be dead when last 6 bits are 100000
                if temp_sequence == list("100000"):
                    #===========================================================
                    # NECSSARY ASSUMPTION: 4 LETTERS AT LEAST
                    #===========================================================
                    if len(self.output) < 4:
                        continue
                    else:
                        return      
            else:
                if self.upper_bound < 0.5:
                    self.e1_rescale()
                elif self.lower_bound >= 0.5:
                    self.e2_rescale()
                # increment index value to realize shift temp sequence
                i += 1
                self.flag = True
                                                              
                
    def update_bounds(self, lower_fx, upper_fx, lower_bound, upper_bound):
        '''Update bounds as soon as a new letter comes'''
        self.lower_bound = lower_bound + (upper_bound - lower_bound) * lower_fx
        self.upper_bound = lower_bound + (upper_bound - lower_bound) * upper_fx
        
    def fx_generation(self):
        '''Calculate the Fx(1), Fx(2), Fx(3), etc. Store these values in fx[]'''
        upper_bound = 0
        for i in self.probabilities:
            lower_bound = upper_bound
            upper_bound += i
            # get a list with 3 items, each item is made of lower Fx and upper Fx
            self.fx.append([lower_bound, upper_bound])

            
    def search_fx(self):
        '''Search range of fx and return lower Fx and upper Fx'''
        for i in range(len(self.fx)):
                if self.temp < self.fx[i][1]:
                    # assign lower value and upper value of Fx[i]
                    lower_fx, upper_fx = self.fx[i][0], self.fx[i][1]
                    self.output.append(self.letters[i])
                    return lower_fx, upper_fx
        
            
    def calc_values(self, temp_sequence):
        '''Calculate temp based on binary codes'''
        temp = 0
        for i in range(len(temp_sequence)):
            if temp_sequence[i] == "1":
                temp += 2 ** (-i-1)
        return temp
    
    def e1_rescale(self):
        '''Realize E1 scale method'''
        self.lower_bound *= 2
        self.upper_bound *= 2
        
    def e2_rescale(self):
        '''Realize E2 scale method'''
        self.lower_bound = 2 * (self.lower_bound - 0.5)
        self.upper_bound = 2 * (self.upper_bound - 0.5)
        
    def get_output(self):
        '''Return output value which contains all the letters'''
        return self.output
        
#------------------------------------------------------------------------------ Encode Instance
# instantiate with SEQUENCE_1
encode_result = Tag_Encode(MODEL, SEQUENCE_2).get_output()
# print sequence list as well as encoded sequence 
print("Encoded result: ", encode_result) 
print("Encoded sequence: ", end = "")
my_encode_sequence = ""
for i in encode_result:
    my_encode_sequence += i
print(my_encode_sequence)
    
#------------------------------------------------------------------------------ Decode Instance
decode_result = Tag_Decode(MODEL, list(my_encode_sequence)).get_output()
print("Decoded result: ", decode_result)
print("Decoded sequence: ", end = "")
my_decode_sequence = ""
for i in decode_result:
    my_decode_sequence += i
print(my_decode_sequence)