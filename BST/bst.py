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
    
def search(root, val, stack):
        # print("hey")
        if root is None:
            return 
        
        if root.data == val:
            stack.append(root)
            return root, stack
        elif root.data <= val:
            if root.right.data == val:
                stack.append(root.right)
                return stack
            else:
                search(root.right, val, stack)
        else:
            if root.left.data == val:
                stack.append(root.left)
                return stack
            else:
                search(root.right, val, stack)

def lca(root, p, q):
        if (p < root.data) and (q < root.data):
            return lca(root.left, p, q)
        if (p > root.data) and (q > root.data):
            return lca(root.right, p, q)
        return root


    
        
        
        
new_Tree=BSTNode(None)
insert(new_Tree, 1)
insert(new_Tree, 3)
insert(new_Tree, 2)
# insert(new_Tree, 23)
# insert(new_Tree, 12)
# insert(new_Tree, 65)
print(new_Tree.data)
print(new_Tree.left.data)
print(new_Tree.right.data)


print(lca(new_Tree, 2, 3).data)    