from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, n in enumerate(nums):
            if n in numDict:
                numDict[n].append(idx)
            else:
                numDict[n] = [idx]
                

        for num in numDict:
            leftover = target - num
            if leftover not in numDict:
                continue
            
            if leftover!=num:
                return numDict[num] + numDict[leftover]
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
                
                
            
#         return False
    
sol1 = Solution()
print(sol1.twoSum2([2,5,5, 11], 10))

#time complexity n + n
#space n