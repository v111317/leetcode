#https://leetcode.com/problems/next-greater-element-i/description/

# The next greater element of some element x in an array is the first greater element that 
# is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine 
# the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer 
# for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)==1:
            return [-1]
        maxNum = -1
        
        result = []
        for num1 in nums1:
            for i, num2 in enumerate(nums2):
                #print(num1, num2)
                if num1==num2:
                    isFound = False
                    for j in range(i+1, len(nums2)):
                        if nums2[j] > num2:
                            result.append(nums2[j])
                            isFound = True
                            break
                    if not isFound:
                        result.append(-1)
                    #print(result)
                    break    
            #print("\n")
        return result

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)==1:
            return [-1]
        
        nums2Len = len(nums2)
        numMap = {}
        numMap[nums2[nums2Len-1]] = -1
        
        numStack = []
        numStack.append(nums2[nums2Len-1])
        
        for i in range(len(nums2)-2, -1, -1):
            topElem = numStack[len(numStack)-1]
            
            if topElem > nums2[i]:
                numStack.append(nums2[i])
                numMap[nums2[i]] = topElem
            else:
                while len(numStack)!=0 and topElem < nums2[i]:
                    numStack.pop()
                    if len(numStack)==0:
                        break
                    topElem = numStack[len(numStack)-1]
                
                if len(numStack)==0:
                    numMap[nums2[i]] = -1
                else:
                    numMap[nums2[i]] = topElem
                numStack.append(nums2[i])
        
        result = []
        for num in nums1:
            result.append(numMap[num])
        return result
                

sol1 = Solution()
#print(sol1.nextGreaterElement2([4,1,2], [1,3,4,2]))
#print(sol1.nextGreaterElement2([2, 4], [1,2,3,4]))

nums1 = [137,59,92,122,52,131,79,236,94,171,141,86,169,199,248,120,196,168,77,71,5,198,215,230,176,87,189,206,115,76,13,216,197,26,183,54,250,27,109,140,147,25,96,105,30,207,241,8,217,40,0,35,221,191,83,132,9,144,12,91,175,65,170,149,174,82,102,167,62,70,44,143,10,153,160,142,188,81,146,212,15,162,103,163,123,48,245,116,192,14,211,126,63,180,88,155,224,148,134,158,119,165,130,112,166,93,125,1,11,208,150,100,106,194,124,2,184,75,113,104,18,210,202,111,84,223,173,238,41,33,154,47,244,232,249,60,164,227,253,56,157,99,179,6,203,110,127,152,252,55,185,73,67,219,22,156,118,234,37,193,90,187,181,23,220,72,255,58,204,7,107,239,42,139,159,95,45,242,145,172,209,121,24,21,218,246,49,46,243,178,64,161,117,20,214,17,114,69,182,85,229,32,129,29,226,136,39,36,233,43,240,254,57,251,78,51,195,98,205,108,61,66,16,213,19,68,237,190,3,200,133,80,177,97,74,138,38,235,135,186,89,201,4,101,151,31,228,231,34,225,28,222,128,53,50,247]
nums2 = [137,59,92,122,52,131,79,236,94,171,141,86,169,199,248,120,196,168,77,71,5,198,215,230,176,87,189,206,115,76,13,216,197,26,183,54,250,27,109,140,147,25,96,105,30,207,241,8,217,40,0,35,221,191,83,132,9,144,12,91,175,65,170,149,174,82,102,167,62,70,44,143,10,153,160,142,188,81,146,212,15,162,103,163,123,48,245,116,192,14,211,126,63,180,88,155,224,148,134,158,119,165,130,112,166,93,125,1,11,208,150,100,106,194,124,2,184,75,113,104,18,210,202,111,84,223,173,238,41,33,154,47,244,232,249,60,164,227,253,56,157,99,179,6,203,110,127,152,252,55,185,73,67,219,22,156,118,234,37,193,90,187,181,23,220,72,255,58,204,7,107,239,42,139,159,95,45,242,145,172,209,121,24,21,218,246,49,46,243,178,64,161,117,20,214,17,114,69,182,85,229,32,129,29,226,136,39,36,233,43,240,254,57,251,78,51,195,98,205,108,61,66,16,213,19,68,237,190,3,200,133,80,177,97,74,138,38,235,135,186,89,201,4,101,151,31,228,231,34,225,28,222,128,53,50,247]
print(sol1.nextGreaterElement2(nums1, nums2))
