#https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes 
# of the first two lists.
# Return the head of the merged linked list
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.num = val
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
    
    def printList(self):
        ptr = self.head
        while ptr!=None:
            print(ptr.num, end=" => ")
            ptr = ptr.next
        print(" ")

ll1 = LinkedList()
ll1.insertAtBegin(6)
ll1.insertAtBegin(5)
ll1.insertAtBegin(1)

ll2 = LinkedList()
ll2.insertAtBegin(4)
ll2.insertAtBegin(3)
ll2.insertAtBegin(2)

ll1.printList()
ll2.printList()
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1==None:
            return list2
        
        if list2==None:
            return list1
        
        ptr1 = list1
        ptr2 = list2
        
        while list2!=None:
            
            while ptr2.num:
                a = 1
            nextptr1 = ptr1.next    
            nextptr2 = ptr2.next
            list2 = nextptr2
            
            if ptr1.num > ptr2.num:
                a = 1
            else:
                ptr1.next = ptr2
                ptr2.next = nextptr1
            ptr1 = ptr2
            ptr2 = list2
            
            
            
        
#sol1 = Solution()
#sol1.mergeTwoLists(ll1.head, ll2.head)