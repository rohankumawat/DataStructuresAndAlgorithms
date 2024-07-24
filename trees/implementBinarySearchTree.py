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
    
    def find_min(self):
        if self.left is None: # if there is no left node, then the current node is the minimum
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        return sum(self.in_order_traversal())
    
    def post_order_traversal(self): # left -> right -> root
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        # visit base node
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self): # root -> left -> right
        elements = []
        # visit base node
        elements.append(self.data)
        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def deleteTakeFromRight(self, val): # O(log n) time complexity
        if val < self.data: # if the value is in the left subtree
            if self.left: # if left node exists
                self.left = self.left.delete(val) # recursively call delete on left node
        elif val > self.data: # if the value is in the right subtree
            if self.right: # if right node exists
                self.right = self.right.delete(val) # recursively call delete on right node
        else: # if the value is the root node (has two children)
            if self.left is None and self.right is None: # if the node is a leaf node (only has a root node)
                return None # delete the node
            if self.left is None: # if the node has only a right child (no left child)
                return self.right # return the right child
            if self.right is None: # if the node has only a left child (no right child)
                return self.left # return the left child
            # if the node has both left and right children
            min_val = self.right.find_min() # find the minimum value in the right subtree
            self.data = min_val # replace the root node with the minimum value
            self.right = self.right.delete(min_val) # delete the minimum value from the right subtree
        return self
    
    def deleteTakeFromLeft(self, val): # O(log n) time complexity
        if val < self.data: # if the value is in the left subtree
            if self.left: # if left node exists
                self.left = self.left.delete(val) # recursively call delete on left node
        elif val > self.data: # if the value is in the right subtree
            if self.right: # if right node exists
                self.right = self.right.delete(val) # recursively call delete on right node
        else: # if the value is the root node (has two children)
            if self.left is None and self.right is None: # if the node is a leaf node (only has a root node)
                return None # delete the node
            if self.left is None: # if the node has only a right child (no left child)
                return self.right # return the right child
            if self.right is None: # if the node has only a left child (no right child)
                return self.left # return the left child
            # if the node has both left and right children
            max_val = self.left.find_max() # find the minimum value in the right subtree
            self.data = max_val # replace the root node with the minimum value
            self.left = self.left.delete(max_val) # delete the minimum value from the right subtree
        return self
    
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    
    print(root.in_order_traversal()) # [1, 4, 9, 17, 18, 20, 23, 34]
    print(root.search(20)) # True
    print(root.search(21)) # False