from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        childrenSum = root.left + root.right
        return root.val == childrenSum
    
tree1 = TreeNode(10, 6, 3)
    
sol1 = Solution()
print(sol1.checkTree(tree1))