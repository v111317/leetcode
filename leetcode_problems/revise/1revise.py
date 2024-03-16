#linked list

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    #at beginning
    def insertNode(self, num):
        
        newNode = Node(num)
        
        if self.head==None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self.head

    def printList(self):
        
        if self.head == None:
            return
        ptr = self.head
        
        while ptr!=None:
            print(" => ", ptr.num, end=" ")
            ptr = ptr.next

        return

# ll1 = LinkedList()
# ll1.insertNode(10)
# ll1.insertNode(1)
# ll1.insertNode(5)
# ll1.insertNode(15)
# ll1.insertNode(20)
# ll1.printList()

class NodeTree:
    
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

class Tree:
    
    def __init__(self):
        self.root = None
        
    def insertNode(self, root, num):
        
        if root == None:
            newNode = NodeTree(num)
            root = newNode
            return root
        
        if num > root.num:
            root.right = self.insertNode(root.right, num)
        else:
            root.left = self.insertNode(root.left, num)
        
        return root

    def printTree(self, root):
        
        if root == None:
            return
        
        self.printTree(root.left)
        print(root.num)
        self.printTree(root.right)
    
t1 = Tree()
t1.root = t1.insertNode(t1.root, 10)
t1.root = t1.insertNode(t1.root, 5)
t1.root = t1.insertNode(t1.root, 15)
t1.root = t1.insertNode(t1.root, 1)
t1.root = t1.insertNode(t1.root, 20)

t1.printTree(t1.root)
        
        