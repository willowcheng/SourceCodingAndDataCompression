'''
#===============================================================================
# Source Coding and Data Compression
# Assignment #1
#===============================================================================

Exercise 3: Use Matlab or other language to implement the encoding and decoding. If 
needed, make necessary assumptions. 

Created on Sep 25, 2014

@author: Liu Cheng
@version: 1.0
'''

MODEL = {1: 0.8, 2 :0.02, 3: 0.18}
SEQUENCE_1 = [1, 3, 2, 1]
SEQUENCE_2 = [3, 2, 1, 1]

class Tag_Generation(object):
    '''Generation of arithmetic encode for given sequence'''
    # initialize lower bound and upper bound with 0 and 1
    lower_bound = 0
    upper_bound = 1
    # Fx(0) is assigned to 0 in very beginning
    fx = []
    # variable temp will be used in temporary storage
    temp = 0

    def __init__(self, model, sequence):
        self.model = model
        self.sequence = sequence
        self.fx_generation(model)
        self.encode_sequence_generate(sequence)
        
    def fx_generation(self, model):
        '''Calculate the Fx(1), Fx(2), Fx(3), etc. Store these values in fx[]'''
        for i in list(self.model.values()):
            temp = self.temp
            self.temp += i
            self.fx.append((temp, self.temp))
            print(self.fx)
        self.temp = 0
        
    def encode_sequence_generate(self, sequence):
        for i in sequence:
            bounds = self.fx[list(self.model.keys()).index(i)]
            lower_bound, upper_bound = bounds[0], bounds[1]
            self.update_bounds(self.lower_bound, self.upper_bound, lower_bound, upper_bound)
        
    def update_bounds(self, lower_bound, upper_bound, lower_fx, upper_fx):
        lower_bound = lower_bound + (upper_bound - lower_bound) * lower_fx
        upper_bound = lower_bound + (upper_bound - lower_bound) * upper_fx
        
        
my_encode_sequence = Tag_Generation(MODEL, SEQUENCE_1)   
        