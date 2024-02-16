from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            match nums[0]:
                case 0:
                    return 1
                case 1:
                    return 0
        
        max = 0
        isZero = False
        for n in nums:
            if n > max:
                max = n
        
        sum = (max * (max + 1))/2
        sum = int(sum)
        
        for n in nums:
            if n==0:
                isZero = True
            sum -= n
            
        if sum==0:
            if isZero:
                return max+1
            else:
                return 0
        else:
            return sum
        
sol1 = Solution()
print(sol1.missingNumber([3, 0, 1]))    
print(sol1.missingNumber([0, 1]))    
print(sol1.missingNumber([1]))    
print(sol1.missingNumber([0]))    
print(sol1.missingNumber([1, 2]))  
        
#time O(n)
#space O(1)