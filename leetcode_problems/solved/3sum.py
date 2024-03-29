#https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
from typing import List

#revise
class Solution:
    #time limit exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numMap = {}
        for n in nums:
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
        
        numMapCopy = numMap.copy()
        
        resultSet = set()
        #print(numMap)
        nums.sort()
        #numArr = list(numMap.keys())
        #print(nums)
        #print(numArr)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                numMap = numMapCopy.copy()
                sum = nums[i] + nums[j]
                #print(i, j, nums[i], nums[j])
                numMap[nums[i]] -= 1
                numMap[nums[j]] -= 1
                remainder = -sum
                # if nums[i] == 0 and nums[j]==0:
                    # print(i, j, nums[i], nums[j], remainder)
                    # print("=>", numMap)
                if remainder in numMap and numMap[remainder] > 0:
                    listItem = [nums[i], nums[j], remainder]
                    listItem.sort()
                    resultSet.add(tuple(listItem))
        
        result = []
        for tup in resultSet:
            result.append(list(tup))
        
        return result
    
    #time limit exceeded
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        
        numMap = {}
        for n in nums:
            if n in numMap:
                numMap[n] += 1
            else:
                numMap[n] = 1
    
        resultSet = set()
        for i in range(len(nums)-2):
            sum = 0 - nums[i]
            j = i + 1
            numMap[nums[i]] -= 1
            while j < len(nums)-1:
                
                num2 = nums[j]
                num3 = sum - num2
                numMap[num2] -= 1
                
                if num3 in numMap and numMap[num3]>0:
                    listItem = [nums[i], nums[j], num3]
                    listItem.sort()
                    resultSet.add(tuple(listItem))
                j += 1
                numMap[num2] += 1
            numMap[nums[i]] += 1
        
        result = []
        for tup in resultSet:
            result.append(list(tup))
        
        return result
    
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()
        resultSet = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                
                sum = nums[i] + nums[j] + nums[k]
                
                if sum==0:
                    listItem = [nums[i], nums[j], nums[k]]
                    resultSet.add(tuple(listItem))
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        
        result = []
        for tup in resultSet:
            result.append(list(tup))
        
        return result
        
sol1 = Solution()
print(sol1.threeSum3([1,2,-2,-1]))
print(sol1.threeSum3([-1,0,1,2,-1,-4]))
print(sol1.threeSum3([0,1,1]))
print(sol1.threeSum3([0,0,0]))
print(sol1.threeSum3([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))

# [[-4,1,3],[-2,1,1],[-2,-2,4],[-4,0,4],[-5,1,4]]
# [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
# print(sol1.threeSum3(list1))
# print(sol1.threeSum3(list2))

#time - O(n*n)
#space - O(1)