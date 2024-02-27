#https://leetcode.com/problems/group-anagrams/description/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        groupMap = {}
        
        for s in strs:
            key = sorted(s)
            key = "".join(key)
            if key in wordMap:
                group = groupMap[key]
                group.append(s)
                groupMap[key] = group
            else:
                wordMap[key] = 1
                groupMap[key] = [s]
        result = []
        for gp in groupMap.values():
            result.append(gp)
        return result

sol1 = Solution()
#print(sol1.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol1.groupAnagrams([""]))
print(sol1.groupAnagrams(["a"]))

#time - O(n*nlogn)
#space - O(n*m) m = number of strings

