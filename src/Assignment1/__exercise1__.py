'''
#===============================================================================
# Source Coding and Data Compression
# Assignment #1
#===============================================================================

Exercise 1: Use Matlab or other language to encode and decode 100 randomly generated 
such blocks. Calculate the bit rate per block. 

Created on Sep 24, 2014

@author: Liu Cheng
@version: 1.1
'''

import random

# 27 elements in total in first proble
INSTANCE_3 = {"a1a1a1":0.512, "a1a1a2":0.0128, "a1a1a3":0.1152, "a1a2a1":0.0128, "a1a2a2":0.00032,
          "a1a2a3":0.00288, "a1a3a1":0.1152, "a1a3a2":0.00288, "a1a3a3":0.02592, "a2a1a1":0.0128,
          "a2a1a2":0.00032, "a2a1a3":0.00288, "a2a2a1":0.00032, "a2a2a2":0.0000008,
          "a2a2a3":0.000072, "a2a3a1":0.00288, "a2a3a2":0.000072, "a2a3a3":0.000648,
          "a3a1a1":0.1152, "a3a1a2":0.00288, "a3a1a3":0.02592, "a3a2a1":0.00288, "a3a2a2":0.000072,
          "a3a2a3":0.000648, "a3a3a1":0.02592, "a3a3a2":0.000648, "a3a3a3":0.005832}

# 9 elements in total in second problem
INSTANCE_2 = {"a1a1":0.64, "a1a2":0.016, "a1a3":0.144, "a2a1":0.016, "a2a2":0.0004, "a2a3":0.036,
              "a3a1":0.144, "a3a2":0.036, "a3a3":0.0324}


class HuffmanItem:
    '''Each HuffmanItem has initial symbol names, probabilities and marked flags'''
    marked = False
    codeword = ""
    left_child = -1
    right_child = -1
    def __init__(self, letter, probability):
        self.letter = letter
        self.probability = probability
        
class Huffman:
    # initialize with list of origin, result and dictionary with code result
    origin = []
    result = []
    codebook = {}
    
    def __init__(self, instance):
        '''Initialize n Huffman items for encoding with elements names and probability'''
        for i in range(len(instance)):
            self.origin.append(HuffmanItem(list(instance.keys())[i], list(instance.values())[i]))
        # initialize list of result which contains 2n-1 items
        # first n items are same as origin[]
        self.result = list(self.origin)
        for i in range(len(self.origin), 2 * len(self.origin) - 1):
            self.result.append(HuffmanItem("", 0))

    def clear_item(self):
        '''Clear processed sequence'''
        self.origin = []
        self.result = []
        self.codebook = {}
        
    def get_min_item(self):
        '''Get letter with minimum probability'''
        index = 0
        probability = 0
        letter = ""
        # compare each letter with previous minimum letter with respect to probability
        for i in range(len(self.result)):
            if not self.result[i].marked and self.result[i].probability > 0:
                if probability == 0 or self.result[i].probability < probability:
                    index = i
                    probability = self.result[i].probability
                    letter = self.result[i].letter
        # once have found minimum letter, marked it
        self.result[index].marked = True
        # return a dictionary which contains index, probability and letter with keys and values
        return {"index":index, "probability":probability, "letter":letter}
    
    def calc_Huffman(self):
        '''Generate new items to fill up blank positions of result[]'''
        # calculate length of origin[] as index for result[]
        index = len(self.origin)
        while index < len(self.result):
            min_item1, min_item2 = self.get_min_item(), self.get_min_item()
            # assign two minimum items with their indices and probabilities addiction
            left_child, probability1 = min_item1["index"], min_item1["probability"]
            right_child, probability2 = min_item2["index"], min_item2["probability"]
            self.result[index].probability = probability1 + probability2
            self.result[index].left_child, self.result[index].right_child = left_child, right_child
            # make sure that all new items are assigned with probability and left child's index as well as right child's
            index += 1
            
    def codeword_assign(self, index, code):
        '''Find left most letter and generate codeword by iteration'''
        self.result[index].codeword += code
        # change indices of children of current letter
        left, right = self.result[index].left_child, self.result[index].right_child
        if left >= 0:
            self.codeword_assign(left, self.result[index].codeword + "0")
        if right >= 0:
            self.codeword_assign(right, self.result[index].codeword + "1")       
            
    def codebook_generate(self):
        '''Assign the codeword for original items and then generate codebook'''
        self.codeword_assign(len(self.result) - 1, "")
        for i in range(len(self.origin)):
            self.codebook[self.result[i].letter] = self.result[i].codeword
            print(self.result[i].letter + ", Huffman Codeword:" + self.result[i].codeword)
        print()

class Test_Module:
    '''Test huffman encode'''
    my_codebook = {}
    my_sequence = []
    def __init__(self, instance):
        my_sequence = Huffman(instance)
        my_sequence.calc_Huffman()
        my_sequence.codebook_generate()
        self.my_codebook = sorted(my_sequence.codebook.items())
        my_sequence.clear_item()
        print(self.my_codebook)
        print()
        
# test_module(INSTANCE_3)
# test_module(INSTANCE_2)

"Testing and generate encode sequence"
encode_sequence = ""
my_codebook = dict(Test_Module(INSTANCE_3).my_codebook)
my_codewords = list(my_codebook.values())
for i in range(100):
    # use random method to randomly pick codewords
    encode_sequence += str(random.choice(my_codewords))
print("Randomly generate 100 encode blocks: ")
print(encode_sequence + "\n")

print("Bit Rate per block is: " + str(len(encode_sequence) / 100) + "bps" + "\n")

class Decode_Huffman:
    def __init__(self, encode_codewords, inverse_codebook):
        self.encode_sequence = encode_codewords
        self.decode_sequence = []
        self.letter = ""
        self.inverse_codebook = inverse_codebook
        # automatic encoding method
        self.encode()
        
    def encode(self):
        '''Use specifics in dictionary to achieve decoding'''
        for i in self.encode_sequence:
            self.letter += i
            # look up inverse my_codebook dictionary
            if self.letter in self.inverse_codebook:
                self.decode_sequence.append(inverse_codebook[self.letter])
                self.letter = ""
                
    def get_decode_sequence(self):
        return self.decode_sequence
                
# generate inverse codebook
inverse_codebook = {value:key for key, value in my_codebook.items()}              
decode_item = Decode_Huffman(list(encode_sequence), inverse_codebook)
decode_sequence = ""
for i in decode_item.get_decode_sequence():
    # expand encode sequence
    decode_sequence += i
print("Encode blocks: ")
print(decode_item.get_decode_sequence())
print("Complete sequence: ")
print(decode_sequence)
                 
