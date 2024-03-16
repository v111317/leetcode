#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        for digit in digits:
            tmp = []
            for letter in digitMap[digit]:
                for subStr in result:
                    tmp.append(subStr+letter)
                if len(result)==0:
                    tmp.append(letter)
            result = tmp
        return result

sol1 = Solution()
print(sol1.letterCombinations("234"))



