#https://leetcode.com/problems/first-bad-version/description/

# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions 
# after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
# bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
import random



class Solution:
    def isBadVersion(self, version: int) -> bool:
        if version >= 4:
            return True
        else:
            return False
    
    def firstBadVersion(self, n: int) -> int:
        if self.isBadVersion(1):
            return 1
        
        start = 1
        end = n
        while start <= end:
            
            mid = (start+end)//2
            print(start, mid, end)
            if self.isBadVersion(mid):
                if mid > 0 and not self.isBadVersion(mid-1):
                    return mid
                else:
                    end = mid - 1
            else:
                if mid < n and self.isBadVersion(mid+1):
                    return mid+1
                else:
                    start = mid + 1
            
    
sol1 = Solution()
print(sol1.firstBadVersion(5))        
            
        
        