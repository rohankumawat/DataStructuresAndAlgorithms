# implementing hash table using Chaining
class HashTable:  
    def __init__(self):
        self.MAX = 10 # max size of the hash table
        self.arr = [[] for i in range(self.MAX)] # creating a list of list
        
    def get_hash(self, key):
        hash = 0 # hash value
        for char in key: # for each character in the key
            hash += ord(char) # ord() returns the Unicode code point for a one-character string
        return hash % self.MAX # hash value modulo max size of the hash table
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key) # get the hash value of the key
        for kv in self.arr[arr_index]: # for each key-value pair in the list
            if kv[0] == key: # if the key matches the key in the list
                return kv[1] # return the value of the key-value pair
        # if the key is not found in the list, python, by-default will return "None"
            
    def __setitem__(self, key, val):
        h = self.get_hash(key) # get the hash value of the key
        found = False # flag to check if the key is found in the list
        for idx, element in enumerate(self.arr[h]): # for each key-value pair in the list
            if len(element)==2 and element[0] == key: # if the key matches the key in the list
                self.arr[h][idx] = (key,val) # update the value of the key-value pair
                found = True # set the flag to True
        if not found: # if the key is not found in the list
            self.arr[h].append((key,val)) # add the key-value pair to the list
        
    def __delitem__(self, key): # delete the key-value pair from the list
        arr_index = self.get_hash(key) # get the hash value of the key
        for index, kv in enumerate(self.arr[arr_index]): # for each key-value pair in the list
            if kv[0] == key: # if the key matches the key in the list
                print("del",index)  # print the index of the key-value pair
                del self.arr[arr_index][index] # delete the key-value pair from the list