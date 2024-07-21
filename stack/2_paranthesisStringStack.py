# Function that checks if paranthesis in a string are balanced or not
# balanced_paranthesis("([])[]({})") should return True
# balanced_paranthesis("([)]") should return False
# balanced_paranthesis("((()") should return False
# balanced_paranthesis("({a+b})") should return True

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

def is_match(ch1, ch2):
    match_dict = {  # dictionary to match the paranthesis
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(string):
    s = Stack() # create a stack object
    for char in string: # for each character in the string
        if char=='(' or char=='[' or char=='{':
            s.push(char)
        elif char==')' or char==']' or char=='}':
            if s.size()==0:
                return False
            if not is_match(char, s.pop()):
                return False
    return s.size()==0

if __name__ == "__main__":
    example = "([])[]({})"
    print(is_balanced(example)) # True
    example = "([)]"
    print(is_balanced(example)) # False
    example = "((()"
    print(is_balanced(example)) # False
    example = "({a+b})"
    print(is_balanced(example)) # True
    example = "({a+b"
    print(is_balanced(example)) # False
    example = "({a+})b"
    print(is_balanced(example)) # True
    example = "[a+b]*(x+2y)*{gg+kk}"
    print(is_balanced(example)) # True