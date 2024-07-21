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

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(10)
    s.push(15)
    print(s)
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())