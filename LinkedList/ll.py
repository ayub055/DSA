class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def prepend(self, value):
        # if the inserted element is the first element
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        
    def append(self, value):
        new_node = node(value)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            self.prepend(value=value)
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
            
            
            
            
            
            