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
        
        #print(" => ", value)
        if root == None:
            print("adding node", value)
            newNode = Node(value)
            root = newNode
            return root
        
        if value > root.num:
            #print("going right")
            root.right = self.insertNode(root.right, value)
        else:
            #print("going left")
            root.left = self.insertNode(root.left, value)
            
        return root
        
    def printTree(self, root):
        # root = self.root
        #print(root.num)
        #print("printing tree")
        if root:
        
            #print("going left")
            self.printTree(root.left)
            print(" => ", root.num)
            #print("going right")
            self.printTree(root.right)
        
        #return 
        

t1 = Tree()
t1.root = t1.insertNode(t1.root, 10)

t1.root = t1.insertNode(t1.root, 20)
t1.root = t1.insertNode(t1.root, 15)
t1.root = t1.insertNode(t1.root, 25)
t1.root = t1.insertNode(t1.root, 5)
t1.root = t1.insertNode(t1.root, 1)
t1.root = t1.insertNode(t1.root, 6)
# print(type(t1))

print("printing tree")
t1.printTree(t1.root)