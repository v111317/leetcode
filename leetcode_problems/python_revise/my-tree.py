class Node:
    
    def __init__(self, value):
        self.num = value
        self.left = None
        self.right = None

#binary tree
class Tree:
    
    def __init__(self):
        self.root = None
        
    def insertNode(self, root, value):
        
        if root == None:
            newNode = Node(value)
            root = newNode
            return root
        
        if value > root.num:
            self.insertNode(root.right, value)
        else:
            self.insertNode(root.left, value)
            
        return root
        
    def printTree(self, root):
        # root = self.root
        
        if root.left!=None:
            self.printTree(root.left)
        
        if root.right!=None:
            self.printTree(root.right)
        
        print(" => ", root.num)
        return 
        
        

t1 = Tree()
t1.insertNode(t1.root, 10)
t1.insertNode(t1.root, 3)
t1.insertNode(t1.root, 8)
t1.insertNode(t1.root, 20)
t1.insertNode(t1.root, 15)
t1.insertNode(t1.root, 25)

t1.printTree(t1.root)