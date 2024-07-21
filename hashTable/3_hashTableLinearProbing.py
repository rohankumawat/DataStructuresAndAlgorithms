# implementing hash table using Linear Probing
class HashTable:  
    def __init__(self):
        self.MAX = 10 # keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)] # creating a list of None
        
    def get_hash(self, key):
        hash = 0 # hash value
        for char in key: # for each character in the key
            hash += ord(char) # ord() returns the Unicode code point for a one-character string
        return hash % self.MAX # hash value modulo max size of the hash table
    
    def __getitem__(self, key):
        h = self.get_hash(key) # get the hash value of the key
        if self.arr[h] is None: # if the key is not found in the list
            return # return None
        prob_range = self.get_prob_range(h) # get the range of the probing
        for prob_index in prob_range: # for each index in the probing range
            element = self.arr[prob_index] # get the element at the index
            if element is None: # if the element is None
                return # return None
            if element[0] == key: # if the key matches the key in the list
                return element[1] # return the value of the key-value pair
           
    def __setitem__(self, key, val):
        h = self.get_hash(key) # get the hash value of the key
        if self.arr[h] is None: # if the key is not found in the list
            self.arr[h] = (key,val) # add the key-value pair to the list
        else: # if the key is found in the list
            new_h = self.find_slot(key, h) # find the new slot for the key
            self.arr[new_h] = (key,val) # add the key-value pair to the list
        print(self.arr) # print the list of key-value pairs
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)] # return the range of the probing
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index) # get the range of the probing
        for prob_index in prob_range: # for each index in the probing range
            if self.arr[prob_index] is None: # if the element is None
                return prob_index # return the index
            if self.arr[prob_index][0] == key: # if the key matches the key in the list
                return prob_index # return the index
        raise Exception("Hashmap full") # raise an exception if the hashmap is full
        
    def __delitem__(self, key):
        h = self.get_hash(key) # get the hash value of the key
        prob_range = self.get_prob_range(h) # get the range of the probing
        for prob_index in prob_range: # for each index in the probing range
            if self.arr[prob_index] is None: # if the element is None
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key: # if the key matches the key in the list
                self.arr[prob_index]=None # delete the key-value pair from the list
        print(self.arr) # print the list of key-value pairs