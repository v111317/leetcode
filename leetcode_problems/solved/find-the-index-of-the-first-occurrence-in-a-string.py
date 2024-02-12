class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
        
sol1 = Solution()
print(sol1.strStr("leetcode", "leeto"))