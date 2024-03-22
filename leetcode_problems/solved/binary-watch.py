#https://leetcode.com/problems/binary-watch/description/

# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent 
# the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".
# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), 
# return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.

# For example, "10:2" is not valid. It should be "10:02".
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        numMap = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8]
        result = []
        for num in range(0, pow(2, 10)):
            i = 0
            minutes = 0
            hours = 0
            setBits = 0
            #print(num)
            while num!=0:
                
                if num & 1 == 1:
                    setBits += 1
                    if i <=5:
                        minutes += numMap[i]
                        if minutes > 59:
                            break
                    else:
                        hours += numMap[i]
                        if hours >= 12:
                            break
                if setBits > turnedOn:
                    break
                num = num >> 1
                i += 1
                #print(" ==> ", hours, minutes)
            
            if num==0 and setBits==turnedOn:
                hours = str(hours)
                # if len(hours)==1:
                #     hours = "0" + hours
                minutes = str(minutes)
                if len(minutes)==1:
                    minutes = "0" + minutes
                timeStr = hours + ":" + minutes
                result.append(timeStr)                            
        
        return result

sol1 = Solution()
# print(sol1.readBinaryWatch(1))
# print(sol1.readBinaryWatch(9))
# print(sol1.readBinaryWatch(6))
print(sol1.readBinaryWatch(2))