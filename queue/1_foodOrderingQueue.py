# food ordering system (Multi-threading)
# producer - consumer problem
# 1. customer can order food
# the thread will be placing an order and inserting it into the queue
# this thread places new order every 0.5 seconds (hint: use time.sleep(0.5))
# 2. server order
# the thread will be serving the order
# this thread serves the order every 2 seconds
# start this thread 1 second after place order thread is started

# pass following as an argument to place order thread:
# orders = ['pizza','samosa','pasta','biryani','burger']

from collections import deque
import threading
import time

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

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()