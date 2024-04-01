#https://leetcode.com/problems/count-binary-substrings/

# Given a binary string s, return the number of non-empty substrings that have the same number of 0's 
# and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)==1:
            return 0
        
        n = len(s)
        count = 0
        i = 0
        while i < n-1:
            j = i
            k = j + 1
            print(j, k)
            if s[j]=="0" and s[k]=="1":
                count += 1
                while j > 0 and k < n-1:
                    j -= 1
                    k += 1
                    if s[j]=="0" and s[k]=="1":
                        count += 1
                    else:
                        break
            elif s[j]=="1" and s[k]=="0":
                count += 1
                while j > 0 and k < n-1:
                    j -= 1
                    k += 1
                    print(" => ", j, k)
                    if s[j]=="1" and s[k]=="0":
                        count += 1
                    else:
                        break
            i += 1
        
        return count
    
sol1 = Solution()
# print(sol1.countBinarySubstrings("00110011"))
# print(sol1.countBinarySubstrings("10101"))
print(sol1.countBinarySubstrings("00110"))
        
                