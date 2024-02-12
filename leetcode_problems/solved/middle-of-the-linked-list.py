from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        headCopy = head
        while(headCopy):
            length += 1
            headCopy = headCopy.next
        #print(length)
        if length%2 == 1:
            steps = math.ceil(length/2)
        else:
            steps = length/2 + 1
            
        steps = int(steps)
        for i in range(1, steps):
            head = head.next
        
        return head
    
    #redo
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head
        
        while(true):
            end = end.next.next
            
        
    
#time complexity - O(n) + O(n/2)
#space complexity - O(1) -  
        