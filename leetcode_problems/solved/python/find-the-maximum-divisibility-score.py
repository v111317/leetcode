#https://leetcode.com/problems/find-the-maximum-divisibility-score/description/

# You are given two 0-indexed integer arrays nums and divisors.

# The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].

# Return the integer divisors[i] with the maximum divisibility score. 
# If there is more than one integer with the maximum score, return the minimum of them.
from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        divisors.sort()
        nums.sort()
        maxDivisions = 0
        maxDivisionsList = []
        count = 0
        
        for div in divisors:
            count = 0
            for num in nums:
                if num%div==0:
                    count += 1
            if count > maxDivisions:
                maxDivisions = count
                maxDivisionsList = [div]
                
            elif count!= 0 and count == maxDivisions:
                maxDivisionsList.append(div)
        
        if len(maxDivisionsList) >= 1:
            return min(maxDivisionsList)
        else:
            return min(divisors)
    
    def maxDivScore2(self, nums: List[int], divisors: List[int]) -> int:
        res = 0 
        count = -1
        for d in divisors:
            curr = sum(1 for i in nums if i%d == 0)
            if curr > count:
                count = curr
                res = d
                print(d, count)
            elif curr == count:
                print(curr, count)
                res = min(res, d)
        return res

sol1 = Solution()
print(sol1.maxDivScore([4,7,9,3,9], [5,2,3]))   
print(sol1.maxDivScore([20,14,21,10], [5,7,5]))   
print(sol1.maxDivScore([1], [1000000000]))  
print(sol1.maxDivScore([56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78], 
                       [39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10,33,72,97,60,79,68,25,63])) 

#time - O(n*n)
#space - O(n)