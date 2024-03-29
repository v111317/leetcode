#https://leetcode.com/problems/baseball-game/description/

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, 
# you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record
# and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer 
# and that all operations are valid.
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:

            
        stk1 = []
        sumNums = 0        
        for op in operations:

            #separate integers and ops
            #print(op)
            if op in ["C", "D", "+"]:
                
                #define - op
                match op:
                    case "C":
                        #print(stk1)
                        num = stk1.pop()
                        sumNums -= num
                    case "D":
                        num = stk1.pop()
                        stk1 += [num, 2*num]
                        sumNums += 2*num
                    case "+":
                        num1 = stk1.pop()
                        num2 = stk1.pop()
                        stk1 += [num2, num1, num1+num2]
                        sumNums += num1+num2
            else:
                #print(op)
                num = int(op)
                stk1.append(num)
                sumNums += num
            print(op, stk1, sumNums)
            
        return sumNums
        
            
sol1 = Solution()
#print(sol1.calPoints(["5","2","C","D","+"]))
print(sol1.calPoints(["5","-2","4","C","D","9","+","+"]))