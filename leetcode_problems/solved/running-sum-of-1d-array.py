#https://leetcode.com/problems/running-sum-of-1d-array/description/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSumList = []
        sum = 0
        for num in nums:
            sum += num
            runningSumList.append(sum)
        return runningSumList

sol1 = Solution()
result = sol1.runningSum([1,2,3])
print(result)

#time - O(1)
#space - O(n)