# You can't use Stacks, Queue, or even array to store
# a heirarchical data structure like a tree. You need tree!

# Implementing a Tree
# A tree is a non-linear data structure that is used to store data in a hierarchical manner.
# It is a collection of nodes connected by edges. Each node contains a value or data,
# and it may or may not have a child node. The topmost node of the tree is called the root node.
# The nodes that have no child nodes are called leaf nodes.
# A tree is a recursive data structure. Each node of the tree may be considered as the root of its subtree.
# A tree is a special case of a graph where no two nodes have the same parent.
# The depth of a node is the number of edges from the root to the node.
# The height of a tree is the maximum depth of any node in the tree.
# The height of a tree with a single node is 0.

class TreeNode:
    def __init__(self, data):
        self.data = data # data of the node (could be string, number, complex object, etc.)
        self.children = [] # this list will be an instance of tree node class. (The child node is a tree node itself)
        self.parent = None # parent of the node (None if the node is the root node)
    
    def add_child(self, child):
        child.parent = self # set the parent of the child node to the current node
        self.children.append(child) # add a child node to the current node
    
    def get_level(self): # get the level of the node
        level = 0 # initialize the level to 0
        p = self.parent # get the parent of the node (you can count the number of parents to get the level)
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3 # get the level of the node
        prefix = spaces + "|__" if self.parent else "" # if the node has a parent, add "|__" to the spaces
        print(prefix + self.data) # print the data of the node
        """
        for child in self.children:
            print("   ", child.data) # print the data of the child node
        """
        if len(self.children) > 0: # if the node has children
            for child in self.children: # lead node doesn't have self.children (it is an empty list/array)
                child.print_tree() # recursively call the print_tree method on the child node

def build_product_tree():
    root = TreeNode("Electronics") # root node

    laptop = TreeNode("Laptop") # child node
    laptop.add_child(TreeNode("Macbook")) # add child node to the child node
    laptop.add_child(TreeNode("Surface")) # add child node to the child node
    laptop.add_child(TreeNode("Thinkpad")) # add child node to the child node

    cellphone = TreeNode("Cell Phone") # child node
    cellphone.add_child(TreeNode("iPhone")) # add child node to the child node
    cellphone.add_child(TreeNode("Google Pixel")) # add child node to the child node
    cellphone.add_child(TreeNode("Samsung Galaxy")) # add child node to the child node

    tv = TreeNode("TV") # child node
    tv.add_child(TreeNode("Samsung")) # add child node to the child node
    tv.add_child(TreeNode("LG")) # add child node to the child node
    tv.add_child(TreeNode("Sony")) # add child node to the child node

    root.add_child(laptop) # add the child node to the root node
    root.add_child(cellphone) # add the child node to the root node
    root.add_child(tv) # add the child node to the root node

    # print(tv.get_level()) # print the level of the tv node
    return root

if __name__ == '__main__':
    root = build_product_tree() # call the function to build the product tree
    # print(root.get_level()) # print the level of the root node
    root.print_tree() # print the tree
    pass