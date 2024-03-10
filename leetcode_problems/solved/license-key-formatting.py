#https://leetcode.com/problems/license-key-formatting/description/

# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. 
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, 
# which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        letterList = []
        for ch in s:
            if ch != "-":
                letterList.append(ch)
                count += 1
        
        groups = count // k
        remainder = count % k
        
        licensePlate = []
        i = 0
        while remainder!=0:
            licensePlate.append(letterList[i])
            remainder -= 1
            i += 1
        if len(licensePlate)!=0 and len(letterList)>len(licensePlate):
            licensePlate.append("-")    
        
        groupLetterCount = k        
        for j in range(i, count):
            licensePlate.append(letterList[j])
            j += 1
            groupLetterCount -= 1
            if groupLetterCount==0 and j!=count:
                licensePlate.append("-")
                groupLetterCount = k
        
        licensePlate = [letter.upper() for letter in licensePlate]
        
        return "".join(licensePlate)
    
sol1 = Solution()
# print(sol1.licenseKeyFormatting("5F3Z-2e-9-w", 4))
# print(sol1.licenseKeyFormatting("2-5g-3-J", 2))
print(sol1.licenseKeyFormatting("2", 2))

#time - O(n)
#space - O(n)

            
                
            
