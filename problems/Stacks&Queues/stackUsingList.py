'''
1. Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.
2. Add a method to push a value onto the Stack.
3. Add a method to pop a value from the Stack.

'''

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    my_stack.print_stack()

    print("Stack before pop():")
    my_stack.print_stack()

    print("\nPopped node:")
    print(my_stack.pop())

    print("\nStack after pop():")
    my_stack.print_stack()
