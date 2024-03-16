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