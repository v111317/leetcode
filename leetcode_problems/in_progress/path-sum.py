class Node:
    
    def __init__(self, value):
        self.num = value
        self.left = None
        self.right = None
    
class Tree:
    
    def __init__(self):
        self.root = None
    
    def insertNode(self, root, value):
        if root ==None:
            root = Node(value)
            return root
    
        if value>root.num:
            root.right = self.insertNode(root.right, value)
        else:
            root.left = self.insertNode(root.left, value)
            
        return root
    
    def printTree(self, root):
        if root:
            self.printTree(root.left)
            print(root.num, " ")
            self.printTree(root.right)
        return
    
    def maxDepth(self, head):
        depth = 0
        if head:
            depth = 1 + max(self.maxDepth(head.left), self.maxDepth(head.right))
               
        return depth 
    
    def hasPathSum(self, root, targetSum):    
        if root.num<targetSum:
            return -1
        
         
        
        
    
t1 = Tree()
t1.root = t1.insertNode(t1.root, 10)
t1.root = t1.insertNode(t1.root, 5)
t1.root = t1.insertNode(t1.root, 20)
t1.root = t1.insertNode(t1.root, 15)
t1.root = t1.insertNode(t1.root, 30)

t1.printTree(t1.root)
print(t1.maxDepth(t1.root))
print(t1.hasPathSum(t1.root, 15))