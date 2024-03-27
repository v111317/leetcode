#https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# A common string is a string that appeared in both list1 and list2.

# A common string with the least index sum is a common string such that if it appeared at 
# list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minIdx = float('+inf')
        
        wordMap = {}
        for i, word in enumerate(list1):
            wordMap[word] = i
            
        result = []
        for i, word in enumerate(list2):
            if word in wordMap:
                idxSum = i + wordMap[word]
                if idxSum == minIdx:
                    result.append(word)
                elif idxSum < minIdx:
                    result = [word]
                    minIdx = idxSum
        return result

sol1 = Solution()
print(sol1.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]))
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

print(sol1.findRestaurant(list1, list2))
                
        