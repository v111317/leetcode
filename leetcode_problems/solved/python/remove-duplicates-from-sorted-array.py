from typing import List

# 30 mins 
# 10 mins think
# 15 mins code
# 5 min revise

#time - O(n2)
#space - O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        countNums = len(nums)
        countDuplicate = 0
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = -1000
                countDuplicate += 1
        
        for i in range(0, len(nums)):
            if nums[i] == -1000:
                
                for j in range(i+1, len(nums)):
                    if nums[j] != -1000 and i < j:
                        nums[i] = nums[j]
                        nums[j] = -1000
                        break
        
        return countNums - countDuplicate
        
        
sol1 = Solution()
#sol1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(sol1.removeDuplicates([1,1,2]))