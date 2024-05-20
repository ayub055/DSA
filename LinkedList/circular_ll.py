class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp = self.head
        result = ""
        
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += " -> "
        return result
            
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
            
        self.length += 1
            
    def insert(self, index, value):
        new_node = Node(value=value)
        if index == 0 or self.head is None:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif index < 0:
            return None
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            
            new_node.next = temp.next
            temp.next = new_node
        self.length + 1
            
    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
            if curr_node == self.head:
                break
            
    def get(self, index):
        if self.head is None:
            return None
        
        if index >= 0 and index <= self.length-1:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value

        else: 
            return None
        
    def set(self, index, value):
        if self.head is None:
            return None
        
        if index >= 0 and index <= self.length-1:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
        return self
    
    def remove(self, index):
        if self.head is None or index < 0 or index > self.length:
            return None
        
        curr_node = self.head
        if index == 0:
            self.head = curr_node.next
            self.tail.next = self.head
            curr_node.next = None
        elif index == self.length - 1:
            for _ in range(index-1):
                curr_node = curr_node.next
            curr_node.next = self.tail.next
            self.temp = self.tail
            self.tail = curr_node
        else: 
            for _ in range(index-1):
                curr_node = curr_node.next
            curr_node.next = self.tail.next
            self.tail = None
            self.tail = curr_node
                        
                           
            
            
listt = CircularList()
listt.append(2)
listt.append(3)
listt.append(4)
listt.prepend(4)
print(listt)
# print(listt.length)

# print(listt.length)
listt.insert(0, -12)
# print(listt)
# listt.traverse()
print(listt.get(0))
print(listt.set(0, 0))
listt.remove(4)
print(listt)
listt.remove(0)
print(listt)






