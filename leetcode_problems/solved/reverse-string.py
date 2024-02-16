from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        iterLen = int(len(s)/2)
        for i in range(0, iterLen):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp

        return s
    
sol1 = Solution()
print(sol1.reverseString(["h","e","l","l","o"]))
print(sol1.reverseString(["H","a","n","n","a","h"]))
print(sol1.reverseString(["H", "a"]))

#time - O(n)
#space - O(1)