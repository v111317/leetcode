#https://leetcode.com/problems/most-common-word/description/

# Given a string paragraph and a string array of the banned words banned, return the most frequent word 
# that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = "!?',;."
        words = paragraph.split(" ")
        words = [word.lower() for word in words]
        
        wordMap = {}
        maxCount = -1
        mostFrequent = ""
        for i, word in enumerate(words):
            strLen = len(word)
            if word[strLen-1] in punctuation:
                newWord = word[0:strLen-1]
                words[i] = newWord
            if words[i] not in banned:
                if words[i] in wordMap:
                    wordMap[words[i]] += 1
                    if wordMap[words[i]] > maxCount:
                        maxCount = wordMap[words[i]]
                        mostFrequent = words[i]
                else:
                    wordMap[words[i]] = 1
                    if maxCount==-1:
                        maxCount = 1
                        mostFrequent = words[i]
        return mostFrequent
        
sol1 = Solution()
print(sol1.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(sol1.mostCommonWord("a, a, a, a, b,b,b,c, c", ["hit"]))

