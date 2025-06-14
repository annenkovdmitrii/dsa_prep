class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
        
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
    def print_queue(self):
        values = []
        temp = self.first
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))
        
# Example usage
if __name__ == "__main__":
    print("Testing Queues:")
    my_queue = Queue(4)
    
    my_queue.print_queue()
    
    print("\nTesting enqueue(6):")
    my_queue.enqueue(6)
    my_queue.print_queue()

    print("\nTesting enqueue(3):")
    my_queue.enqueue(3)
    my_queue.print_queue()
    
    print("\nTesting enqueue(8):")
    my_queue.enqueue(8)
    my_queue.print_queue()
    
    print("\nTesting dequeue 1:")
    my_queue.dequeue()
    my_queue.print_queue()
    
    print("\nTesting dequeue 2:")
    my_queue.dequeue()
    my_queue.print_queue()
    
    print("\nTesting dequeue 3:")
    my_queue.dequeue()
    my_queue.print_queue()
    
    print("\nTesting dequeue 4:")
    my_queue.dequeue()
    my_queue.print_queue()
    
