
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
                
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value: # value is in the left side of the tree
                temp = temp.left
            elif value > temp.value: # value is in the right side of the tree
                temp = temp.right
            else:
                return True # value is found
        return False # value is not found (we reached the end of the tree)
    
    # Method 1: In-order traversal (prints values in sorted order)
    def print_tree(self):
        """Prints BST values in sorted order using in-order traversal"""
        if self.root is None:
            print("Tree is empty")
            return
        
        def in_order(node):
            if node is not None:
                in_order(node.left)   # Visit left subtree
                print(node.value, end=" ")  # Visit root
                in_order(node.right)  # Visit right subtree
        
        print("In-order traversal: ", end="")
        in_order(self.root)
        print()  # New line

    # Method 2: Visual tree structure (hierarchical)
    def print_tree_visual(self):
        """Prints a visual representation of the tree structure"""
        if self.root is None:
            print("Tree is empty")
            return
            
        def print_helper(node, prefix="", is_left=True):
            if node is not None:
                print(prefix + ("├── " if is_left else "└── ") + str(node.value))
                
                # Print children
                if node.left is not None or node.right is not None:
                    if node.left is not None:
                        print_helper(node.left, prefix + ("│   " if is_left else "    "), True)
                    else:
                        print(prefix + ("│   " if is_left else "    ") + "├── None")
                    
                    if node.right is not None:
                        print_helper(node.right, prefix + ("│   " if is_left else "    "), False)
                    else:
                        print(prefix + ("│   " if is_left else "    ") + "└── None")
        
        print("Tree structure:")
        print(str(self.root.value))
        if self.root.left is not None or self.root.right is not None:
            if self.root.left is not None:
                print_helper(self.root.left, "", True)
            else:
                print("├── None")
            
            if self.root.right is not None:
                print_helper(self.root.right, "", False)
            else:
                print("└── None")

    # Method 3: Vertical tree with branches (like traditional tree diagrams)
    def print_tree_vertical(self):
        """Prints tree in vertical format with / and \ branches"""
        if self.root is None:
            print("Tree is empty")
            return
        
        def get_height(node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(self.root)
        
        # Collect all nodes by level with their positions
        def collect_nodes():
            if not self.root:
                return []
            
            levels = []
            queue = [(self.root, 0, 0)]  # (node, level, position)
            
            while queue:
                node, level, pos = queue.pop(0)
                
                # Ensure we have enough levels
                while len(levels) <= level:
                    levels.append([])
                
                levels[level].append((node.value if node else None, pos))
                
                if node and level < height - 1:
                    # Add children to next level
                    queue.append((node.left, level + 1, pos * 2))
                    queue.append((node.right, level + 1, pos * 2 + 1))
            
            return levels
        
        levels = collect_nodes()
        
        print("Vertical tree:")
        
        # Calculate the width needed for the bottom level
        max_width = 2 ** (height - 1) if height > 0 else 1
        node_width = 4  # Space allocated per node
        total_width = max_width * node_width
        
        for level_idx, level_nodes in enumerate(levels):
            # Calculate spacing for this level
            nodes_at_level = 2 ** level_idx
            spacing_between = total_width // nodes_at_level if nodes_at_level > 0 else total_width
            first_node_offset = spacing_between // 2
            
            # Create the line for node values
            line = [' '] * total_width
            positions = []
            
            for i, (value, _) in enumerate(level_nodes):
                if value is not None:
                    pos = first_node_offset + i * spacing_between
                    value_str = str(value)
                    start_pos = pos - len(value_str) // 2
                    
                    # Place the value
                    for j, char in enumerate(value_str):
                        if 0 <= start_pos + j < total_width:
                            line[start_pos + j] = char
                    
                    positions.append(pos)
                else:
                    positions.append(None)
            
            print(''.join(line).rstrip())
            
            # Print branches for all levels except the last
            if level_idx < height - 1:
                branch_line = [' '] * total_width
                
                for i, pos in enumerate(positions):
                    if pos is not None:
                        # Calculate positions of children
                        left_child_pos = first_node_offset // 2 + (i * 2) * (spacing_between // 2) if level_idx + 1 < len(levels) else None
                        right_child_pos = first_node_offset // 2 + (i * 2 + 1) * (spacing_between // 2) if level_idx + 1 < len(levels) else None
                        
                        # Check if children exist
                        left_exists = (i * 2 < len(levels[level_idx + 1]) and 
                                     levels[level_idx + 1][i * 2][0] is not None)
                        right_exists = (i * 2 + 1 < len(levels[level_idx + 1]) and 
                                      levels[level_idx + 1][i * 2 + 1][0] is not None)
                        
                        # Draw branches
                        if left_exists and pos - 1 >= 0:
                            branch_line[pos - 1] = '/'
                        if right_exists and pos + 1 < total_width:
                            branch_line[pos + 1] = '\\'
                
                branch_line_str = ''.join(branch_line).rstrip()
                if branch_line_str:  # Only print if there are branches
                    print(branch_line_str)
        
        print()

        
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")
   
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [47, 21, 76, 18, 27, 52, 82]
    
    for value in values:
        bst.insert(value)
    
    print("BST created with values:", values)
    print()
    
    # Print sorted values
    bst.print_tree()
    print()
    
    # Print hierarchical tree structure
    bst.print_tree_visual()
    print()
    
    # Print vertical tree with branches
    bst.print_tree_vertical()

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
    
    print("\n----- Test: Contains on Empty Tree -----\n")
    bst = BinarySearchTree()
    result = bst.contains(5)
    check(False, result, "Check if 5 exists in an empty tree:")

    print("\n----- Test: Contains Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    result = bst.contains(10)
    check(True, result, "Check if 10 exists:")
    result = bst.contains(5)
    check(True, result, "Check if 5 exists:")
    result = bst.contains(15)
    check(True, result, "Check if 15 exists:")

    print("\n----- Test: Contains Not Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    result = bst.contains(15)
    check(False, result, "Check if 15 exists:")

    print("\n----- Test: Contains with Duplicate Inserts -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    result = bst.contains(10)
    check(True, result, "Check if 10 exists with duplicate inserts:")

    print("\n----- Test: Contains with Left and Right -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(1)
    bst.insert(8)
    bst.insert(12)
    bst.insert(20)
    result = bst.contains(1)
    check(True, result, "Check if 1 exists:")
    result = bst.contains(8)
    check(True, result, "Check if 8 exists:")
    result = bst.contains(12)
    check(True, result, "Check if 12 exists:")
    result = bst.contains(20)
    check(True, result, "Check if 20 exists:")
