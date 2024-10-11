
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def reverse(head):
    # Atleast 2 nodes should be there
    if head is None or head.next is None:
        return head
    
    prev = None 
    curr = head 
    nextP = head.next
    
    while curr :
        curr.next = prev  # Pointing back
        # Shifting the pointers
        prev = curr
        curr= nextP
        if nextP:
            nextP = nextP.next
            
    return prev
    
    
def rec_reverse1(head):
    if not head or not head.next:
         return
    else:
        rec_reverse1(head.next)
        head.next.next = head
    
    
def rec_reverse2(head):
    if head is None or head.next is None:
        return head
    
    new_head = rec_reverse2(head.next)
    head.next.next = head
    head.next = None
    return new_head
    
    
def rec_reverse3(head, prev):
    if head is None:
        return prev
    
    curr = rec_reverse3(head.next, head)
    head.next = prev
    
    return curr

    
def rec_reverse4(head, prev):
    if head is None:
        return prev
    
    nextP = head.next
    head.next = prev
    
    return rec_reverse4(nextP, head)

# Utility function to print the linked list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Utility function to append data to the list
def append(head, data):
    if not head:
        return Node(data)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)
    return head

# Example Usage
head = None
head = append(head, 1)
head = append(head, 2)
head = append(head, 3)
head = append(head, 0)

print("Original list:")
print_list(head)

# For first version discussed in lectures -- START
# last = head
# while last.next:
#     last = last.next
# rec_reverse(head)
# head.next = None
# head = last
# For first version discussed in lectures -- END

head = rec_reverse4(head, prev=None)

print("List after reversing ")
print_list(head)







    