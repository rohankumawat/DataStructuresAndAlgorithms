class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data ==self.data:
            return # value/node already exists (cant have duplicates)
        
        if data < self.data:
            # add data in left subtree
            if self.left: # check if left node exists already
                self.left.add_child(data)
            else: # if left node does not exist, create it
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self): # left -> root -> right
        elements = []
        # visit left tree
        if self.left: # means you have a left node / have some elements in left subtree
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, val): # O(log n) time complexity
        if self.data == val: # if the value is the root node
            return True
        
        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    
    print(root.in_order_traversal()) # [1, 4, 9, 17, 18, 20, 23, 34]
    print(root.search(20)) # True
    print(root.search(21)) # False