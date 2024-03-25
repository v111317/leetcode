#https://leetcode.com/problems/remove-linked-list-elements/description/

# Given the head of a linked list and an integer val, remove all the nodes of the linked 
# list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        ptr = head
        prev = ptr
        isFound = False
        isFirst = True
        
        while ptr!=None:
            if ptr.val==val:
                isFound = True
                
            else:
                if isFirst:
                    head = ptr
                    isFirst = False
                    
                if isFound:
                    prev.next = ptr
                    isFound = False
                prev = ptr
            ptr = ptr.next
        
        if isFirst:
            head = None
        
        if isFound:
            prev.next = ptr
            
        return head    