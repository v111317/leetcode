class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = 1
        s = s.strip()
        wordsList = s.split(" ")
        wordsCount = len(wordsList)
        print(wordsList)
        return len(wordsList[wordsCount-1])

#time - O(n)
#space - O(n)
    
sol1 = Solution()
print(sol1.lengthOfLastWord("   fly me   to   the moon  "))
        