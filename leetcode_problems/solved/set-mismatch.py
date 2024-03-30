#https://leetcode.com/problems/set-mismatch/description/

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, 
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number 
# and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numMap = {}
        dupNum = -1
        for num in nums:
            if num in numMap:
                dupNum = num
            else:
                numMap[num] = 1
        
        missingNum = -1
        for i in range(1, len(nums)+1):
            if i not in numMap:
                missingNum = i
        
        return [dupNum, missingNum]

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        
        #using xor
        

sol1 = Solution()
print(sol1.findErrorNums2([1,2,2,4]))        
#print(sol1.findErrorNums2([1,1]))