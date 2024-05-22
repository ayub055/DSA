class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class Queue:
    def __init__(self) -> None:
        self.items = LinkedList()
        self.length = 0
        
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        return self.items.head == None
    
    def enqueue(self, value):
        item = Node(value)
        if self.items.head is None:
            self.items.head = item
            self.items.tail = item
        else:
            self.items.tail.next = item
            self.items.tail = item
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no node in queue"
        else:
            temp = self.items.head
            if self.items.head == self.items.tail:
                self.items.head = None
                self.items.tail = None
            else:
                self.items.head = self.items.head.next
            return temp


        