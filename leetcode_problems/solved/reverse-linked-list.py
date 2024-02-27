#https://leetcode.com/problems/reverse-linked-list/

#Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import Optional


# Definition for singly-linked list.
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
        
        return self.head
    
    def printList(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.val, end=" => ")
            ptr = ptr.next
        print(" ")




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = head
        
        if head==None or ptr1.next==None:
            return head
        
        ptr2 = ptr1.next
        if ptr2.next!=None:
            ptr3 = ptr2.next
        else:
            ptr2.next = ptr1
            ptr1.next = None
            return ptr2
        
        while ptr3!=None:
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
            ptr3 = ptr3.next
        
        ptr2.next = ptr1
        head.next = None
    
        return ptr2
    
ll1 = LinkedList()
ll1.insertAtBegin(5)
ll1.insertAtBegin(4)
# ll1.insertAtBegin(3)
# ll1.insertAtBegin(2)
# ll1.insertAtBegin(1)
ll1.printList()

sol1 = Solution()
ll1.head = sol1.reverseList(ll1.head)
ll1.printList()
           