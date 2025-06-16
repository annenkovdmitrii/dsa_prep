class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def print_node(self):
        next_val = self.next.value if self.next else None
        print(f"Node({self.value}) | Next: {next_val}")

class LinkedList:
    def __init__(self, value):
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
        values.append("None")
        print(" -> ".join(values))
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        pre = self.head
        temp = self.head
        if self.length == 0:
            return None
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None  
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None   
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): # we use _ because we are not using a variable in the foor loop
            temp = temp.next
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
            return False # if we successfully insert item, we return True, otherwise False
        if index == 0:
            return self.prepend(value) 
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None # if we remove a Node successfully we return it, otherwise we return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(sewalf.length):
            after = temp.next
            temp.next = before # reversing the pointer
            before = temp # bringing up the pointer to the newxt Node
            temp = after
        
        
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")
        
# Example usage
if __name__ == "__main__":
    print("\n----- Test: Pop on linked list with one node -----\n")
    linked_list = LinkedList(1)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(1, popped_node.value, "Value of popped node:")
    check(None, linked_list.head, "Head of linked list:")
    check(None, linked_list.tail, "Tail of linked list:")
    check(0, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop on linked list with multiple nodes -----\n")
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(3, popped_node.value, "Value of popped node:")
    check(1, linked_list.head.value, "Head of linked list:")
    check(2, linked_list.tail.value, "Tail of linked list:")
    check(2, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop on empty linked list -----\n")
    linked_list = LinkedList(1)
    linked_list.head = None
    linked_list.tail = None
    linked_list.length = 0
    popped_node = linked_list.pop()
    check(None, popped_node, "Popped node from empty linked list:")
    check(None, linked_list.head, "Head of linked list:")
    check(None, linked_list.tail, "Tail of linked list:")
    check(0, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop all -----\n")
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(2, popped_node.value, "Value of popped node (first pop):")
    check(1, linked_list.head.value, "Head of linked list (after first pop):")
    check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
    check(1, linked_list.length, "Length of linked list (after first pop):")
    popped_node = linked_list.pop()
    check(1, popped_node.value, "Value of popped node (second pop):")
    check(None, linked_list.head, "Head of linked list (after second pop):")
    check(None, linked_list.tail, "Tail of linked list (after second pop):")
    check(0, linked_list.length, "Length of linked list (after second pop):")
    popped_node = linked_list.pop()
    check(None, popped_node, "Popped node from empty linked list (third pop):")
    check(None, linked_list.head, "Head of linked list (after third pop):")
    check(None, linked_list.tail, "Tail of linked list (after third pop):")
    check(0, linked_list.length, "Length of linked list (after third pop):")

    print("\nPrepend TESTS:\n")
    my_linked_list = LinkedList(2)
    my_linked_list.append(3)

    print('Before prepend():')
    print('----------------')
    print('Head:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length, '\n')
    print('Linked List:')
    my_linked_list.print_list()


    my_linked_list.prepend(1)


    print('\n\nAfter prepend():')
    print('---------------')
    print('Head:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length, '\n')
    print('Linked List:')
    my_linked_list.print_list()

    print("\nPop_first TESTS:\n")
    my_linked_list = LinkedList(2)
    my_linked_list.append(1)
    my_linked_list.print_list()

    # (2) Items - Returns 2 Node
    print(my_linked_list.pop_first().value)
    # (1) Item -  Returns 1 Node
    print(my_linked_list.pop_first().value)
    # (0) Items - Returns None
    print(my_linked_list.pop_first())

    print("\nGet TESTS:\n")
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.print_list()
    print("my_linked_list.get(3).value = ", my_linked_list.get(3).value)

    print("\nSet_value TESTS:\n")
    my_linked_list = LinkedList(11)
    my_linked_list.append(3)
    my_linked_list.append(23)
    my_linked_list.append(7)

    print('LL before set_value(1,4)):')
    my_linked_list.print_list()

    my_linked_list.set_value(1,4)

    print('\nLL after set_value(1,4):')
    my_linked_list.print_list()

    print("\nInsert TESTS:\n")
    my_linked_list = LinkedList(1)
    my_linked_list.append(3)


    print('LL before insert():')
    my_linked_list.print_list()


    my_linked_list.insert(1,2)

    print('\nLL after insert(2) in middle:')
    my_linked_list.print_list()


    my_linked_list.insert(0,0)

    print('\nLL after insert(0) at beginning:')
    my_linked_list.print_list()


    my_linked_list.insert(4,4)

    print('\nLL after insert(4) at end:')
    my_linked_list.print_list()

    print("\nRemove TESTS:\n")
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    print('LL before remove():')
    my_linked_list.print_list()

    print('\nRemoved node:')
    print(my_linked_list.remove(2).value)
    print('LL after remove() in middle:')
    my_linked_list.print_list()

    print('\nRemoved node:')
    print(my_linked_list.remove(0).value)
    print('LL after remove() of first node:')
    my_linked_list.print_list()

    print('\nRemoved node:')
    print(my_linked_list.remove(2).value)
    print('LL after remove() of last node:')
    my_linked_list.print_list()