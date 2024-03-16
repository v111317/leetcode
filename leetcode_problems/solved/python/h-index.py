#https://leetcode.com/problems/h-index/description/

# Given an array of integers citations where citations[i] is the number of citations a researcher 
# received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such 
# that the given researcher has published at least h papers that have each been cited at least h times.
from typing import List

#revise
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==1:
            return min(citations[0], 1)
        
        citations.sort()
        hIdx = 0
        
        for i in range(len(citations)):
            j = i
            count = 0
            while j < len(citations):
                # print(i, j, hIdx)
                if citations[j]>= citations[i]:
                    count += 1        
                    if count>=citations[i]:
                        hIdx = citations[i]
                        break
                else:
                    break
                j += 1
            if count < citations[i]:
                hIdx = max(hIdx, count)
            # print(" => ", hIdx)
        return hIdx
    
    def hIndex2(self, citations: List[int]) -> int:
        if len(citations)==1:
            return min(citations[0], 1)
        citations.sort()
        hIdx = len(citations)
        for num in citations:
            if num < hIdx:
                hIdx -= 1
        
        return hIdx
    
sol1 = Solution()
print(sol1.hIndex2([3,0,6,1,5]))
print(sol1.hIndex2([1,3,1]))
print(sol1.hIndex2([100]))
print(sol1.hIndex2([11, 15]))

#solution 1
#time - O(n*n)
#space - (1)

#solution 2
#time - O(nlogn)
#space - O(1)