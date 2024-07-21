# implement Queue using deque

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

if __name__ == "__main__":
    q = Queue()
    
    q.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })
    print(q)
    print(q.size())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())