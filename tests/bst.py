
# In a FULL tree EVERY node points to either:
# Zero Nodes OR two nodes

# In a PERFECT tree:
# Any level in the tree that has any nodes 
# is complitely filled all the way accross 

# In a COMPLETE tree
# The nodes are filled only from left to right
# with no gaps

# Every Node can only have one Parent Node

# BinarySearchTree
# NO DUPLICATES
# Child Nodes are on the left if the value is less
# then the parent and on the right if the value 
# of the child node is greater than the parent

# So for any given node in BST, the nodes
# on the left of it will be less than that node
# and all the nodes on the right will be
# greater than that node 

# Big-O of BST:
# Average:
# Search - O(log(n))
# Insert - O(log(n))
# Access - O(log(n))
# Deletion - O(log(n))

# Worst:
# Search - O(n)
# Insert - O(n)
# Access - O(n)
# Deletion - O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value) # creates new node
        if self.root is None: # handles the empty tree
            self.root = new_node
            return True
        temp = self.root # declaring a temp value
        while (True): # we will breakout of that while loop by hitting the return statement
            if new_node.value == temp.value:
                return False # the if ensures no duplicates in BST
            if new_node.value < temp.value:
                if temp.left is None: # left spot is open
                    temp.left = new_node
                    return True
                temp = temp.left # move to the left node
            else: 
                if temp.right is None: # right spot is open
                    temp.right = new_node
                    return True
                temp = temp.right # moved to the right node
 
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")
   
if __name__ == "__main__":

    print("\n----- Test: Insert to Empty Tree -----\n")
    bst = BinarySearchTree()
    result = bst.insert(5)
    check(True, result, "Insert 5, should succeed:")
    check(5, bst.root.value, "Root value after inserting 5:")
    check(None, bst.root.left, "Root's left child after inserting 5:")
    check(None, bst.root.right, "Root's right child after inserting 5:")

    print("\n----- Test: Insert to Existing Tree -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    result = bst.insert(3)
    check(True, result, "Insert 3, should succeed:")
    check(3, bst.root.left.left.value, "Root's left-left value after inserting 3:")
    check(None, bst.root.left.left.left, "Root's left-left-left child after inserting 3:")
    check(None, bst.root.left.left.right, "Root's left-left-right child after inserting 3:")

    print("\n----- Test: Insert Duplicate Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    result = bst.insert(5)
    check(False, result, "Insert 5 again, should fail:")
    check(None, bst.root.left.left, "Root's left-left child after inserting 5 again:")
    check(None, bst.root.left.right, "Root's left-right child after inserting 5 again:")

    print("\n----- Test: Insert Greater Than Root -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    result = bst.insert(15)
    check(True, result, "Insert 15, should succeed:")
    check(15, bst.root.right.value, "Root's right value after inserting 15:")
    check(None, bst.root.right.left, "Root's right-left child after inserting 15:")
    check(None, bst.root.right.right, "Root's right-right child after inserting 15:")

    print("\n----- Test: Insert Less Than Root -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    result = bst.insert(5)
    check(True, result, "Insert 5, should succeed:")
    check(5, bst.root.left.value, "Root's left value after inserting 5:")
    check(None, bst.root.left.left, "Root's left-left child after inserting 5:")
    check(None, bst.root.left.right, "Root's left-right child after inserting 5:")