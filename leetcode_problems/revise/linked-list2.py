class Node:
    
    def __init__(self, value):
        self.num = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, value):
        newNode = Node(value)
        ptr = self.head
        newNode.next = ptr
        self.head = newNode
        
    def printList(self):
        ptr  = self.head
        while ptr!=None:
            print(ptr.num)
            ptr = ptr.next
            
ll1 = LinkedList()
ll1.insertAtBeginning(10)
ll1.insertAtBeginning(5)
ll1.insertAtBeginning(50)
ll1.insertAtBeginning(20)

ll1.printList()