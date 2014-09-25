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
    output = []

    def __init__(self, model, sequence):
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
            self.fx.append([temp, self.temp])
        
    def encode_sequence_generate(self, sequence):
        for i in sequence:
            bounds = self.fx[self.letters.index(i)]
            lower_fx, upper_fx = bounds[0], bounds[1]
            self.update_bounds(lower_fx, upper_fx, self.lower_bound, self.upper_bound)
            while (self.upper_bound < 0.5 or self.lower_bound >= 0.5):
                if self.upper_bound < 0.5:
                    self.e1_scale()
                    self.output.append("0")
                elif self.lower_bound >= 0.5:
                    self.e2_scale()
                    self.output.append("1")
        self.output.append("100000")
            
    def update_bounds(self, lower_fx, upper_fx, lower_bound, upper_bound):
        self.lower_bound = lower_bound + (upper_bound - lower_bound) * lower_fx
        self.upper_bound = lower_bound + (upper_bound - lower_bound) * upper_fx
        
    def e1_scale(self):
        self.lower_bound *= 2
        self.upper_bound *= 2
        
    def e2_scale(self):
        self.lower_bound = 2 * (self.lower_bound - 0.5)
        self.upper_bound = 2 * (self.upper_bound - 0.5)
        
    def get_output(self):
        return self.output

    def clear(self):
        self.fx = []
        self.temp = 0
        self.output = []
        self.lower_bound = 0
        self.upper_bound = 1
        self.model = {}
        self.sequence = []
        
my_encode_sequence = Tag_Encode(MODEL, SEQUENCE_1).get_output() 
print("Result: ") 
print(my_encode_sequence) 
print("Encoded sequence: ")
for i in my_encode_sequence:
    print(i, end="")
my_encode_sequence.clear()