class Node: # Node class
    def __init__(self, data=None, next=None, prev=None):
        self.data = data # Data
        self.next = next # Next node
        self.prev = prev # Previous node

class DoubleLinkedList: # Double linked list class
    def __init__(self):
        self.head = None
    
    # Insert at the beginning
    def insertAtBeginning(self, data):
        if self.head is None: # If the linked list is empty
            node = Node(data, None, None)
            self.head = node
        else: # If the linked list is not empty
            node = Node(data, self.head, None) # Create a new node
            self.head.prev = node # Set the previous node of the head to the new node
            self.head = node # Set the head to the new node
    
    # Print the linked list
    def printForward(self):
        if self.head is None: # If the linked list is empty
            print("Linked list is empty")
            return
        itr = self.head # Iterator
        llstr = '' # Linked list string
        while itr:
            llstr += str(itr.data) + ' --> ' # Add the data to the string
            itr = itr.next # Move to the next node
        print("Linked List in forward: ", llstr) # Print the linked list
    
    def getLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    # Print the linked list in reverse
    def printBackward(self):
        if self.head is None: # If the linked list is empty
            print("Linked list is empty")
            return
        # itr = self.head
        # while itr.next: # Move to the last node
        #     itr = itr.next # Move to the next node
        lastNode = self.getLastNode()
        itr = lastNode # Iterator
        llstr = ''
        while itr: # Print the linked list in reverse
            llstr += str(itr.data) + ' --> '
            itr = itr.prev
        print("Linked List in reverse: ", llstr)

    # get the length
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    