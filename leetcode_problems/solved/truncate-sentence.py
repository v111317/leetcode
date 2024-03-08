#https://leetcode.com/problems/truncate-sentence/description/

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. 
# Return s​​​​​​ after truncating it.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = 1
        words = s.split(" ")
        words = [words[i] for i in range(k)]
        return " ".join(words)
    
sol1 = Solution()
print(sol1.truncateSentence("Hello how are you Contestant", 4))
print(sol1.truncateSentence("What is the solution to this problem", 4))

#time - O(n)
#space - O(n)

    