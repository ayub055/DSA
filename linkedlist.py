class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        temp = self.head
        result = ""
        
        while temp is not None:
            result += str(temp.val)
            if temp.next is not None:
                result += " -> "
            temp = temp.next
            
        return result
        
    def append(self, val):
        curr_node = ListNode(val)
        if not self.head:
            self.head = curr_node
            self.tail = curr_node
        else:
            self.tail.next = curr_node
            self.tail = curr_node
            
            
class Solution:
    def merge_two_ll(self, list1, list2):
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
            
        while l1.next or l2.next:
            if list1.val > list2.val:
                list2 = list2.next
            else:
                list1 = list1.next
                
    def reverse(self, head):
        curr_node = head
        left = None

        while curr_node:
            right = curr_node.next
            curr_node.next = left
            left = curr_node
            curr_node = right
        
        return left
            

        

l1 = LinkedList()
l2 = LinkedList()

l1.append(1)
l1.append(2)
l1.append(4)

l2.append(1)
l2.append(3)
l2.append(4)

print(l1)
print(l2)



obj = Solution()
print(obj.merge_two_ll(l1, l2))