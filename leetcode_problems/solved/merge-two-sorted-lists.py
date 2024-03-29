#https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes 
# of the first two lists.
# Return the head of the merged linked list
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:    
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, value):
        newNode = ListNode(value)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return
    
    def printList(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.val, end=" => ")
            ptr = ptr.next
        print(" ")
        return


        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #def mergeTwoLists(self, list1, list2):
        
        ptr = list1
        #print(typeof(ptr))
        while ptr!=None:
            print(ptr.val, end=" => ")
            ptr = ptr.next
        print(" ")
        
        ptr = list2
        while ptr!=None:
            print(ptr.val, end=" => ")
            ptr = ptr.next
        print(" ")
        
        if list1==None and list2==None:
            return None
        
        if list1==None:
            return list2
        
        if list2==None:
            return list1
        
        ptr1 = list1
        ptr2 = list2
        ptr3 = None
        
        head3 = None
        #count = 0
        isFirst = True
        
        while ptr1!=None and ptr2!=None:
            
            if ptr1.val > ptr2.val:
                if isFirst:
                    ptr3 = ptr2
                else:
                    ptr3.next = ptr2
                    ptr3 = ptr3.next
                ptr2 = ptr2.next
            else:
                if isFirst:
                    ptr3 = ptr1
                else:
                    ptr3.next = ptr1
                    ptr3 = ptr3.next
                ptr1 = ptr1.next
            
            if isFirst:
                head3 = ptr3
                isFirst = False
             
            # if ptr3.next!=None:
            #     ptr3 = ptr3.next
            
            # ll3 = LinkedList()
            # ll3.head = head3
            # ll3.printList()
                
        if ptr2==None:
            ptr3.next = ptr1
            
        if ptr1==None:
            ptr3.next = ptr2
        
        return head3
        
ll1 = LinkedList()
ll1.insertAtBegin(4)
ll1.insertAtBegin(2)
ll1.insertAtBegin(1)

ll2 = LinkedList()
ll2.insertAtBegin(4)
ll2.insertAtBegin(3)
ll2.insertAtBegin(1)     

# ll1.printList()
# ll2.printList()       
        
sol1 = Solution()
head3 = sol1.mergeTwoLists(ll1.head, ll2.head)

ll3 = LinkedList()
ll3.head = head3
ll3.printList()
