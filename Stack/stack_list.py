class Stack:
    def __init__(self):
        self.stack = []
        
    def __str__(self):
        values = [str(x) for x in reversed(self.stack)]
        return " ".join(values)
    
    def isEmpty(self):
        return len(self.stack) == 0 
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.isEmpty():
            return "No element to pop"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "No element to peek in Stack"
        return self.stack[-1]
    
cs = Stack()
cs.push(1)
cs.push(2)
cs.push(3)
print(cs)

print(cs.isEmpty())
# print(cs.peek())
# print(cs)
print(cs.pop())
print(cs)

