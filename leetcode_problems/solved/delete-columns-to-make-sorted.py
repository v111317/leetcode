#https://leetcode.com/problems/delete-columns-to-make-sorted/description/

# You are given an array of n strings strs, all of the same length.

# The strings can be arranged such that there is one on each line, making a grid.

# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), 
# columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, 
# so you would delete column 1.

# Return the number of columns that you will delete.
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        colDelCount = 0
        
        cols = len(strs[0])
        rows = len(strs)
        
        if rows == 1:
            return 0
        
        for i in range(cols):
            for j in range(rows-1):
                if strs[j][i] > strs[j+1][i]:
                    colDelCount += 1
                    break
        
        return colDelCount

sol1 = Solution()
print(sol1.minDeletionSize(["cba","daf","ghi"]))
print(sol1.minDeletionSize(["a","b"]))
print(sol1.minDeletionSize(["zyx","wvu","tsr"]))
