class Solution:
    def isPalindrome(self, x: int) -> bool:
        cloneNum = 0
        num = x
        while x != 0:
            cloneNum *= 10
            cloneNum += x % 10
            
            x /= 10
            x = int(x)
            #print(cloneNum)
        
        return cloneNum == num

sol1 = Solution()
print(sol1.isPalindrome(252))

#time log n
#space O(1)