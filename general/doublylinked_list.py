class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def print_node(self):
        prev_val = self.prev.value if self.prev else None
        next_val = self.next.value if self.next else None
        print(f"Node({self.value}) | Prev: {prev_val} | Next: {next_val}")

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        
        if values:
            print("None <- " + " <-> ".join(values) + " -> None")
        else:
            print("None <- None -> None")
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1): # for loop iterating backwards from indewx of tail to index
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        # Has to return True OR False
        if index < 0 or index > self.length:
            return False # Wasn't able to insert
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next # O(1) instead of a second get with O(n)
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        
        return temp

            
# Example usage
if __name__ == "__main__":
    print("Testing Doubly Linked List:\n")
    
    print("Initial Doubly Linked List:")
    my_doubly_linked_list = DoublyLinkedList(7)
    
    my_doubly_linked_list.print_list()
    
    print("\nTesting Append:")
    
    print("\nAppend(9):")
    my_doubly_linked_list.append(9)
    my_doubly_linked_list.print_list()
    
    print("\nAppend(3):")
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.print_list()
    
    print("\nAppend(1):")
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.print_list()
    
    print("\nTesting Pop:")
    
    print("\nPop 1:")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_list()
    
    print("\nPop 2:")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_list()
    
    print("\nPop 3:")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_list()
    
    print("\nPop 4:")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_list()
    
    print("\nTesting Prepend:")
    
    print("\nPrepend(9):")
    my_doubly_linked_list.prepend(9)
    my_doubly_linked_list.print_list()
    
    print("\nPrepend(3):")
    my_doubly_linked_list.prepend(3)
    my_doubly_linked_list.print_list()
    
    print("\nPrepend(1):")
    my_doubly_linked_list.prepend(1)
    my_doubly_linked_list.print_list()
    
    print("\nTesting Pop_first:")
    
    print("\nPop_first 1:")
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    
    print("\nPop_first 2:")
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    
    print("\nPop_first 3:")
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    
    print("\nPop_first 4:")
    my_doubly_linked_list.pop_first()
    my_doubly_linked_list.print_list()
    
    print("\nTesting Get:")
    my_doubly_linked_list.append(3)
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.append(4)
    my_doubly_linked_list.append(2)
    my_doubly_linked_list.print_list()
    
    print("\nGet value at index 2:")
    print("Get(2):",my_doubly_linked_list.get(2).value)
    
    print("\nGet value at index 4:")
    print("Get(2):",my_doubly_linked_list.get(4).value)
    
    print("\nTesting Set_value:")
    my_doubly_linked_list.print_list()
    print("\nSet value at index 2 to be 99:")
    my_doubly_linked_list.set_value(2, 99)
    my_doubly_linked_list.print_list()
    
    print("\nSet value at index 4 to be 30:")
    my_doubly_linked_list.set_value(4, 30)
    my_doubly_linked_list.print_list()
    
    print("\nTesting Insert:")
    my_doubly_linked_list.print_list()
    
    print("\nInsert value at index 4 to be 1:")
    my_doubly_linked_list.insert(4, 1)
    my_doubly_linked_list.print_list()
    
    print("\nInsert value at index 1 to be 12:")
    my_doubly_linked_list.insert(1, 12)
    my_doubly_linked_list.print_list()
    
    print("\nTesting Remove:")
    my_doubly_linked_list.print_list()
    
    print("\nRemoving node at index 1:")
    my_doubly_linked_list.remove(1)
    my_doubly_linked_list.print_list()
    
    print("\nRemoving node at index 5:")
    my_doubly_linked_list.remove(5)
    my_doubly_linked_list.print_list()
    
    print("\nRemoving node at index 3:")
    my_doubly_linked_list.remove(3)
    my_doubly_linked_list.print_list()