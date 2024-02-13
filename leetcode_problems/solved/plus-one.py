from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        addOne = True
        carryover = 0
        
        for i in range(len(digits)-1, -1, -1):
            
            digitSum = digits[i] + carryover + int(addOne)
            addOne = False
            
            digits[i] = digitSum % 10
            carryover = int(digitSum / 10)
        
        newDigit = []
        if carryover > 0:
            newDigit = [1]
        
        return newDigit + digits
    
sol1 = Solution()
#print(sol1.plusOne([9, 9, 9]))
#print(sol1.plusOne([3, 2, 1]))

#time - O(n)
#space - O(1)