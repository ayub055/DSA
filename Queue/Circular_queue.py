class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1
        self.start = -1
        
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif (self.top+1 == self.size) and (self.start == 0):
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        
        else:
            if self.top + 1 == self.size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        
        rem_elem = self.items[self.start]
        self.items[self.start] = None
        if self.start + 1 == self.size:
            self.start == 0
        elif self.start == self.top:
            self.start = -1
            self.top = -1
        else:
            self.start += 1
        return rem_elem
    
q = CircularQueue(3)
q.enqueue(1)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.start, q.top, q.size)

q.enqueue(6)
# q.dequeue()
print(q)

