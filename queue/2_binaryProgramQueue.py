# print binary numbers from 1 to n using a queue
"""
Binary Sequence using Queue should look like:
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque() # using deque to implement queue

    def enqueue(self, data):
        self.queue.appendleft(data) # append data to the queue

    def dequeue(self):
        if len(self.queue) == 0:
            return None # if the queue is empty, return None
        return self.queue.pop() # pop the first element from the queue
    
    def is_empty(self):
        return len(self.queue) == 0 # return True if the queue is empty, else False
    
    def size(self):
        return len(self.queue) # return the size of the queue
    
    def __str__(self):
        return str(self.queue) # return the queue as a string
    
    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[-1] # return the front element of the queue

def generate_binary_numbers(n):
    q = Queue()
    q.enqueue("1")
    for i in range(n):
        front = q.front()
        print("   ", front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        q.dequeue()

if __name__ == "__main__":
    generate_binary_numbers(10) # pass the number to generate binary numbers