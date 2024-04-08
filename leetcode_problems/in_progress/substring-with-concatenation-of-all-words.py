#https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" 
# are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lenWord = len(words[0])
        countWords = len(words)
        
        wordMap = {}
        wordMapCopy = {}
        for word in words:
            if word in wordMap:
                wordMap[word] += 1
            else:
                wordMap[word] = 1
            
        substrLen = lenWord * countWords
        
        endIdx = len(s)
        
        wordsList = []
        i = 0
        result = []
        isFirst = True
        
        while i < endIdx:
            wordMapCopy = wordMap.copy()
            print(i, wordsList)
            if isFirst:
                start = i
                end = i + substrLen
                isFirst = False
            else:
                start = end
                end += lenWord
            
            while start < end:
                wordsList.append(s[start:start+lenWord])
                # print(start, end, wordsList)
                start += lenWord
            
            count = 0
            print(" => ", i, wordsList)
            for word in wordsList:
                if word in wordMapCopy and wordMapCopy[word]>0:
                    wordMapCopy[word] -= 1
                    count += 1
                    # del wordMapCopy[word]
            if count==countWords:
                result.append(i)
                
            i += lenWord
            if len(wordsList)>0:
                wordsList.pop(0)
        
        return result
            

sol1 = Solution()
# print(sol1.findSubstring("barfoothefoobarman", ["foo", "bar"]))
# print(sol1.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
# print(sol1.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
# print(sol1.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(sol1.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))



