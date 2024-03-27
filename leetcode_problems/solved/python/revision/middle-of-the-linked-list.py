#https://leetcode.com/problems/middle-of-the-linked-list/description/

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return head
        
        listLen = 0
        ptr = head
        while ptr!=None:
            listLen += 1
            ptr = ptr.next
        
        steps = listLen//2 + 1
        
        ptr = head
        for i in range(1, steps):
            ptr = ptr.next
        
        return ptr
    
    #solve using slow and fast pointer using only 1 pass
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head
        
        while(true):
            end = end.next.next
            
        
    
#time complexity - O(n) + O(n/2)
#space complexity - O(1) -  
        