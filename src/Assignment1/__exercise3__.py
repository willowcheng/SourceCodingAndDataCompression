'''
#===============================================================================
# Source Coding and Data Compression
# Assignment #1
#===============================================================================

Exercise 3: Use Matlab or other language to implement the encoding and decoding. If 
needed, make necessary assumptions. 

Created on Sep 25, 2014

@author: Liu Cheng
@version: 1.2
'''

LETTERS = ["1", "2" , "3"]
PROBABILITIES = [0.8, 0.02, 0.18]
MODEL = [LETTERS, PROBABILITIES]
SEQUENCE_1 = ["1", "3", "2", "1"]
SEQUENCE_2 = ["3", "2", "1", "1"]

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
        
# instantiate with SEQUENCE_1
my_encode_sequence = Tag_Encode(MODEL, SEQUENCE_1).get_output()
# print sequence list as well as encoded sequence 
print("Result: ", my_encode_sequence) 
print("Encoded sequence: ", end="")
for i in my_encode_sequence:
    print(i, end="")