class BSTNode:
    def __init__(self, data) -> None:
        pass
        self.data = data
        self.left = None
        self.right = None
        
def insert(root, new_node_val):
    if root.data is None:
        root.data = new_node_val
    
    elif root.data <= new_node_val:
        if root.right is None:
            new_node = BSTNode(data = new_node_val)
            root.right = new_node
        else:
            insert(root.right, new_node_val)
    
    else:
        if root.left is None:
            new_node = BSTNode(data = new_node_val)
            root.left = new_node
        else:
            insert(root.left, new_node_val)
      
                
def preorder(root):
    if root is None:
        return
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)
    
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
def search(self, root, val, stack):
        print("hey")
        
        if root.data == val:
            stack.append(root)
            return root, stack
        elif root.data <= val:
            if root.right.data == val:
                stack.append(root.right)
                return root.right, stack
            else:
                self.search(root.right, val, stack)
        else:
            if root.left.data == val:
                stack.append(root.left)
                return root.left, stack
            else:
                self.search(root.right, val, stack)

def lowestCommonAncestor(self, root, p, q):
    p_val = p.data
    q_val = q.data

    stack_p = []
    stack_q = []


    
        
        
        
new_Tree=BSTNode(None)
insert(new_Tree, 50)
insert(new_Tree, 70)
insert(new_Tree, 40)
insert(new_Tree, 23)
insert(new_Tree, 12)
insert(new_Tree, 65)

# preorder(new_Tree)
# print("-" * 50)
# inorder(new_Tree)
stack = []
temp, s = search(new_Tree, 12, stack)
print(temp.data)
print(s)

              