class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) :
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
        
    def print_stack(self):
        temp = self.top
        print(None)
        while temp is not None:
            print(" |")
            print("",temp.value)
            
            temp = temp.next



if __name__ == "__main__":
    print("Test Stack:\n")
    my_stack = Stack(2)
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(5)
    my_stack.push(7)
    my_stack.print_stack()
    
    print("\nPoping from the stack 1:\n")
    my_stack.pop()
    my_stack.print_stack()
    print("\nPoping from the stack 2:\n")
    my_stack.pop()
    my_stack.print_stack()
    print("\nPoping from the stack 3:\n")
    my_stack.pop()
    my_stack.print_stack()