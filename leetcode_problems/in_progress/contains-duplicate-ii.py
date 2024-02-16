from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums)<=1:
            return False
        
        for i in range(0, len(nums)):
            for j in range(i+1, i+k+1):
                
                if j > 1:
                    True
                
                if nums[i]==nums[j]:
                    return True
                
            if i==len(nums)-1-k:
                break
        
        return False
    
sol1 = Solution()
# print(sol1.containsNearbyDuplicate([1,2,3,1], 2))
# print(sol1.containsNearbyDuplicate([1,0,1,1], 1))
# print(sol1.containsNearbyDuplicate([1,2,3,1,2,3], 2))
# print(sol1.containsNearbyDuplicate([99,99], 2))
print(sol1.containsNearbyDuplicate([1, 2], 2))

#time - O(n)
#space - O(1)