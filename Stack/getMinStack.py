class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.length = 0
        self.min = None
        
    def push(self, val):
        if val < self.min:
            self.min = val
        self.stack.append(val)
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            print("No element to pop")
            return
        else:
                    