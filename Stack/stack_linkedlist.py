class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
        

class Stack:
    def __init__(self):
        self.stack = LinkedList()
        
    def __str__(self):
        values = [str(x.value) for x in self.stack]
        return " ".join(values)
        
    def isEmpty(self):
        return not self.stack.head
    
    def push(self, value):
        new_elem = Node(value)
        new_elem.next = self.stack.head
        self.stack.head = new_elem
        
    def pop(self):
        if self.isEmpty():
            return "No element to pop"
        else:
            temp = self.stack.head
            self.stack.head = temp.next
            return temp.value
        
cs = Stack()
cs.push(100)
cs.push(400)
cs.push(200)
print(cs)
cs.pop()
print(cs)
        