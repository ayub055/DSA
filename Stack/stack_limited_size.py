class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.length = 0
        
    def isEmpty(self):
        return self.length == 0
    
    def isFull(self):
        return self.length == self.size
    
    def push(self, value):
        if self.isFull():
            return "Stack Size Exceeded!!!"
        else:
            self.length += 1
            self.stack.append(value)
            
    def pop(self):
        if self.isEmpty():
            return "No element to pop from stack"
        else:
            self.length -= 1
            return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "No element to peep from stack"
        else:
            return self.stack[-1]
    
            