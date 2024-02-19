#https://leetcode.com/problems/linked-list-cycle/description/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, pos is used to denote the
# index of the node that tail's next pointer is connected to. Note that pos is not passed
# as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        
        if head.next!=None:
            hare = head.next
        else:
            return False
        
        tort = head
        while hare.next!=None or tort.next!=None:
            if hare==tort:
                return True
            if hare.next!=None and hare.next.next!=None:
                hare = hare.next.next
            else:
                return False
            
            if tort.next!=None:
                tort = tort.next
            else:
                return False
            
        return False