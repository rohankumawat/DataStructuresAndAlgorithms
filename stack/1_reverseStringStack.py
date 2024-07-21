# Function in python that can reverse a string using Stack data structure
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque() # using deque to implement stack

    def push(self, data):
        self.stack.append(data) # append data to the stack

    def pop(self):
        if len(self.stack) == 0:
            return None # if the stack is empty, return None
        return self.stack.pop() # pop the last element from the stack

    def peek(self):
        if len(self.stack) == 0:
            return None # if the stack is empty, return None
        return self.stack[-1] # return the last element of the stack

    def size(self):
        return len(self.stack) # return the size of the stack

    def is_empty(self):
        return len(self.stack) == 0 # return True if the stack is empty, else False

    def __str__(self):
        return str(self.stack) # return the stack as a string

def reverse_string(string):
    s = Stack() # create a stack object
    reversed_string = "" # initialize an empty string
    for char in string: # for each character in the string
        s.push(char) # push the character to the stack
    while not s.is_empty(): # while the stack is not empty
        reversed_string += s.pop()
    return reversed_string # return the reversed string

if __name__ == "__main__":
    example = "We will conquere COVID-19"
    print(reverse_string(example)) # 91-DIVOC ereuqnoc lliw eW