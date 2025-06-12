class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        """Initialize linked list with a single node containing value"""
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print the linked list"""
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
            
    def append(self, value):
        """Add a new node with the given value at the end of the list. O(1) time complexity."""
        new_node = Node(value)
        
        if self.head is None:
            # If the list is empty, set head and tail to the new node.
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail to the new node.
            self.tail = new_node
        self.length += 1
        
        

# Example usage
if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    
    print(my_linked_list.head.value)  
    
    
    # # Add elements
    # my_linked_list.append(1)
    # my_linked_list.append(2)
    # my_linked_list.append(3)
    # my_linked_list.prepend(0)
    # print(f"List: {my_linked_list}")  # 0 -> 1 -> 2 -> 3 -> None
    
    # # Insert at position
    # my_linked_list.insert(2, 1.5)
    # print(f"After insert: {ll}")  # 0 -> 1 -> 1.5 -> 2 -> 3 -> None
    
    # # Delete elements
    # ll.delete(1.5)
    # print(f"After delete: {ll}")  # 0 -> 1 -> 2 -> 3 -> None
    
    # # Access elements
    # print(f"Element at index 2: {ll.get(2)}")  # 2
    # print(f"Index of element 3: {ll.find(3)}")  # 3
    # print(f"Size: {len(ll)}")  # 4
