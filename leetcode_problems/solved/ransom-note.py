class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        magLetters = [*magazine]
        
        magDict = {}
        for l in magLetters:
            if l in magDict:
                magDict[l] += 1
            else:
                magDict[l] = 1
        
        lettersFound = 0
        
        #print(magDict)
        
        for l in ransomNote:
            if l in magDict and magDict[l] > 0:
                magDict[l] -= 1
                lettersFound += 1
            else:
                return False
            
        return lettersFound == len(ransomNote)
        
sol1 = Solution()
print(sol1.canConstruct("aa", "bba"))

#time - O(no. of magazine letters)
#space - O(26) - distinct letters 