#https://leetcode.com/problems/string-compression/description/

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1

        n = len(chars)
        count = 1
        startIdx = 0
        for i in range(1, n):
            #print(i, startIdx, chars)
            if chars[i]==chars[i-1]:
                count += 1
                # if i==n-1:
                #     print(" => ", "match and in n-1 ", count)
                #     chars[startIdx] = chars[i-1]
                #     startIdx += 1
                #     if count > 1 and count < 10:
                #         chars[startIdx] = str(count)
                #         startIdx += 1
                #     elif count >= 10:
                #         lenCount = len(str(count))
                #         j = lenCount
                #         while count!=0:
                            
                #             digit = count % 10
                #             count = count // 10
                #             chars[startIdx+j-1] = str(digit)
                #             j -= 1
                #         startIdx += lenCount
                #     count = 1
            else:
                chars[startIdx] = chars[i-1]
                startIdx += 1
                if count > 1 and count < 10:
                    chars[startIdx] = str(count)
                    startIdx += 1
                elif count >= 10:
                    lenCount = len(str(count))
                    j = lenCount
                    while count!=0:
                        
                        digit = count % 10
                        count = count // 10
                        chars[startIdx+j-1] = str(digit)
                        j -= 1
                    startIdx += lenCount
                count = 1
            if i==n-1:
                #print(" => ", startIdx)
                chars[startIdx] = chars[i]
                startIdx += 1
                if count > 1 and count < 10:
                    chars[startIdx] = str(count)
                    startIdx += 1
                elif count >= 10:
                    lenCount = len(str(count))
                    j = lenCount
                    while count!=0:
                        
                        digit = count % 10
                        count = count // 10
                        chars[startIdx+j-1] = str(digit)
                        j -= 1
                    startIdx += lenCount
                count = 1
        #print(chars)    
        return startIdx
    
    
sol1 = Solution()
print(sol1.compress(["a","a","b","b","c","c","c"]))  
print(sol1.compress(["a"]))            

print(sol1.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

print(sol1.compress(["a", "b", "c"]))
print(sol1.compress(["o","o","o","o","o","o","o","o","o","o"]))
