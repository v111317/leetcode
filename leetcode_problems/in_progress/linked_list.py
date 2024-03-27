class ListNode:
    
    def __init__(self, value):
        self.val = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertAtStart(self, value):
        node1 = ListNode(value)
        
        if self.head != None:
            node1.next = self.head
        
        self.head = node1
        return
    
    def insertAtEnd(self, value):
        node1 = ListNode(value)
        
        if self.head==None:
            self.head = node1
            return
        
        ptr  = self.head
        
        while ptr.next!=None:
            ptr = ptr.next
        
        ptr.next = node1
        return   
    
    def insertAtIndex(self, value, idx):
        #if list is empty - insert at 1
        #if list len less than idx - insert at end
        #else insert at position
        
        node1 = ListNode(value)
        
        if self.head==None:
            self.head = node1
            return
        
        ptr  = self.head
        
        count = 0 
        while ptr.next!=None:
            if count==idx-1:
                node1.next = ptr.next
                ptr.next = node1
                return
            
            count += 1
            ptr = ptr.next
        
        ptr.next = node1
        return 

    
        
    
    
    def printList(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.val, " -> ", end="")
            ptr = ptr.next
        print("")
        return
            
            
            
# ll1 = LinkedList()
# ll1Head = None
# for i in range(10):
#     ll1.insertAtStart(i)

# # ll1.printList()

# for i in range(5):
#     ll1.insertAtEnd(i)


# ll1.printList()
# ll1.insertAtIndex(101, 4)
# ll1.printList()
# ll1.insertAtIndex(102, 15)
# ll1.printList()
# ll1.insertAtIndex(103, 1000)
# ll1.printList()
