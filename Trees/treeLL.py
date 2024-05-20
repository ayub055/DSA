class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
root = TreeNode(45)
left1 = TreeNode(20)
right1 = TreeNode(34)
root.left = left1
root.right = right1

def preOrder(root):
    if root is None:
        return
    
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
# preOrder(root)

def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)
    
# postOrder(root)
    
def inOrder(root):
    if root is None: 
        return
    
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

inOrder(root)


