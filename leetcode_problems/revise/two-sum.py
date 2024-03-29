#https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, n in enumerate(nums):
            if n in numDict:
                numDict[n].append(idx)
            else:
                numDict[n] = [idx]
        
        #print(numDict)        

        for num in numDict:
            leftover = target - num
            if leftover not in numDict:
                continue
            
            if leftover!=num:
                return numDict[num] + numDict[leftover] #concatenate two arrays
            else:
                if len(numDict[num])==2:
                    return numDict[num]
    #better         
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        
        for idx, n in enumerate(nums):
            if n in numsDict:
                return [numsDict[n], idx]
            else:
                numsDict[target-n] = idx
                

    
sol1 = Solution()
print(sol1.twoSum([2,7,11,15], 9))

#solution 1
#time - O(n)
#space - O(n)

#solution 2
#time - O(n)
#space - O(n)
