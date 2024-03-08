#https://leetcode.com/problems/replace-all-digits-with-characters/description/

# You are given a 0-indexed string s that has lowercase English letters in its even indices and 
# digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

class Solution:
    def replaceDigits(self, s: str) -> str:
        newStr = []
        for i, ch in enumerate(s):
            if i%2==0:
                newStr.append(s[i])
            else:
                letter = chr(ord(s[i-1]) + int(s[i]))
                newStr.append(letter)
        return "".join(newStr)

sol1 = Solution()
print(sol1.replaceDigits("a1c1e1"))
print(sol1.replaceDigits("a1b2c3d4e"))

#time - O(n)
#space - O(1)