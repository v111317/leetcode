from typing import List
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = math.floor(len(nums)/2)
        numMap = {}
        for n in nums:
            if n in numMap:
                numMap[n] += 1
                if numMap[n] > count:
                    break
            else:
                numMap[n] = 1
        
        return n
#time - O(n)
#space - O(n)


    
    #boyer-moore majority vote algorithm
    def majorityElement2(self, nums: List[int]) -> int:
        candidate = nums[0]
        votes = 0
        
        for n in nums:
            if votes==0:
                candidate = n
            
            if n==candidate:
                votes += 1
            else:
                votes -= 1
                
        return candidate
    
#time - O(n)
#space - O(1)
        
    
sol1 = Solution()
print(sol1.majorityElement2([2,2,1,1,1,2,2]))
print(sol1.majorityElement2([3,2,3]))


