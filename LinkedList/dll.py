class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def __str__(self):
        temp = self.head
        result = ""
        
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " <-> "
            temp = temp.next
            
        return result
    
    def traverse_till(self, index):
        if index < 0 and index > self.length - 1:
            return None
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        
dll = DoublyLL()
dll.append(20)
dll.append(10)
dll.append(2)
dll.append(7)
dll.append(4)
dll.append(0)

n = dll.traverse_till(6)
print(n.value)
        