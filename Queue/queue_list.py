class Queue:
    def __init__(self):
        self.items = []
        self.length = 0
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        return self.length==0
    
    def enqueue(self, value):
        self.length += 1
        self.items.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return "No element in Queue"
        else:
            return self.items.pop(0)
        
    