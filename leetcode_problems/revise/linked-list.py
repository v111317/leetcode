class Node:
    def __init__(self, value):
        self.num = value
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def printList(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.num)
            ptr = ptr.next
            
    def insertAtPosition(self, value, index):
        newNode = Node(value)
        ptr = self.head
        # nextPtr = self.head
        currentIdx = 0
        while currentIdx!=index and ptr!=None:
            ptr = ptr.next
            currentIdx += 1
        nextPtr = ptr.next
        ptr.next = newNode
        newNode.next = nextPtr
    
    #0-indexed
    def insertAtPositionExact(self, value, index):
        newNode = Node(value)
        ptr = self.head
        # nextPtr = self.head
        currentIdx = 0
        while ptr!=None and currentIdx<index-1:
            ptr = ptr.next
            currentIdx += 1
        if index==0:
            newNode.next = ptr
            self.head = newNode
        else:
            nextPtr = ptr.next
            ptr.next = newNode
            newNode.next = nextPtr        

ll1 = LinkedList()

ll1.insertAtBegin(5)
ll1.insertAtBegin(15)
ll1.insertAtBegin(1)
ll1.insertAtBegin(23)
ll1.insertAtPositionExact(10, 0)

ll1.printList()
        
        