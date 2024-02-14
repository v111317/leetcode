class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        copyStr = s.lower()
        letters = [l for l in copyStr if l.isalpha() or l.isnumeric()]
        copyStr = "".join(letters)
        orgStr = copyStr[::-1]
        return copyStr == orgStr
        
sol1 = Solution()
print(sol1.isPalindrome(" fmkf ,v fvff"))
print(sol1.isPalindrome("A man, a plan, a canal: Panama"))
#time - O(n)
#space - O(n)