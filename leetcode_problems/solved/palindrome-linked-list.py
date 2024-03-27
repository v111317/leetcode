#https://leetcode.com/problems/palindrome-linked-list/

#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from linked_list import LinkedList
from linked_list import ListNode
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        
        ptr = head
        num = 0
        stk1 = []
        while ptr!=None:
            stk1.append(ptr.val)
            ptr = ptr.next
            
        ptr = head
        n = len(stk1)
        
        for i in range(n//2):
            if ptr.val==stk1.pop():
                ptr=ptr.next
            else:
                return False
        
        return True

ll1 = LinkedList()
ll1.insertAtStart(1)
ll1.insertAtStart(2)
ll1.insertAtStart(3)
ll1.insertAtStart(1)

sol1 = Solution()
print(sol1.isPalindrome(ll1.head))
        
        