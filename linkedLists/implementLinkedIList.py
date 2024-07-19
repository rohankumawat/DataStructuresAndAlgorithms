# Description: Implementing a linked list in python
class Node: # Node class
    def __init__(self, data=None, next=None): # Constructor
        self.data = data # Data
        self.next = next # Next node

class LinkedList: # Linked list class
    def __init__(self): # Constructor
        self.head = None # Head Node
    
    def insertAtBeginning(self, data): # Insert at beginning
        node = Node(data, self.head) # Create a new node
        self.head = node # Set the head to the new node
    
    def print(self): # Print the linked list
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head # Iterator
        llstr = '' # Linked list string
        while itr:
            llstr += str(itr.data) + ' --> ' # Add the data to the string
            itr = itr.next # Move to the next node
        print(llstr)
    
    def insertAtEnd(self, data): # Insert at the end
        if self.head is None:
            self.head = Node(data, None) # If the linked list is empty, add the node to the head
            return
        itr = self.head # Iterator
        while itr.next:
            itr = itr.next # Move to the next node
        itr.next = Node(data, None) # Add the new node to the end
    
    def getLength(self):
        count = 0 # Counter
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insertAt(self, index, data):
        if index < 0 or index >= self.getLength(): # Check if the index is valid
            raise Exception("Invalid index")
        
        if index == 0: # Insert at the beginning
            self.insertAtBeginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # Insert the node
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)
    
    def insertAfterValue(self, data_after, data_to_insert):
        # Search for first occurence of data_after in the linked list
        # Now insert data_to_insert after data_after node
        itr = self.head # Iterator
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
    
    def removeByValue(self, data):
        # Remove the first node that contains data
        if self.head is None: #
            return
        
        if self.head.data == data: # If the head contains the data
            self.head = self.head.next # Move the head to the next node
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtEnd(5)
    ll.insertAtEnd(10)
    ll.insertAtEnd(15)
    ll.insertAtEnd(20)
    ll.insertAtEnd(25)
    ll.print()
    ll.insertAtBeginning(0)
    ll.print()
    ll.insertAt(3, 12)
    ll.print()
    ll.removeAt(3)
    ll.print()
    ll.insertValues([1, 2, 3, 4, 5])
    ll.print()
    ll = LinkedList()
    ll.insertValues(["banana","mango","grapes","orange"])
    ll.print()
    ll.insertAfterValue("mango","apple") # insert apple after mango
    ll.print()
    ll.removeByValue("orange") # remove orange from linked list
    ll.print()
    ll.removeByValue("figs")
    ll.print()
    ll.removeByValue("banana")
    ll.removeByValue("mango")
    ll.removeByValue("apple")
    ll.removeByValue("grapes")
    ll.print()