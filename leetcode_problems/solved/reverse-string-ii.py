#https://leetcode.com/problems/reverse-string-ii/description/

# Given a string s and an integer k, reverse the first k characters for every 2k characters 
# counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than 
# or equal to k characters, then reverse the first k characters and leave the other as original.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<=1:
            return s
        i = 0
        result = []
        while i < len(s):
            if i%(2*k) < k:
                
                j = min(i+k-1, len(s)-1)
                count = j - i + 1
                while count > 0:
                    result.append(s[j])
                    j -= 1
                    i += 1
                    count -= 1
            else:
                result.append(s[i])
                i += 1
        return "".join(result)
sol1 = Solution()
print(sol1.reverseStr("abcdefg", 2))
print(sol1.reverseStr("abcd", 2))
print(sol1.reverseStr("abcdefg", 3))

#time - O(n)
#space - O(n)