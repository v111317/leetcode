class Node:
    
    def __init__(self, value):
        self.num = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, value):
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def printList(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.num, end=" => ")
            ptr = ptr.next
        
ll1 = LinkedList()
ll1.insertAtBeginning(10)
ll1.insertAtBeginning(4)
ll1.insertAtBeginning(15)
ll1.insertAtBeginning(25)
ll1.insertAtBeginning(9)
ll1.insertAtBeginning(30)

ll1.printList()