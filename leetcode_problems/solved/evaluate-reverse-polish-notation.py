#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokensLen = len(tokens)
        stk1 = []
        
        for token in tokens:
            #token = tokens[i]
            
            if token not in ["+", "-", "/", "*"]:
                stk1.append(int(token))
            else:
                num1 = stk1.pop()
                num2 = stk1.pop()
                result = 0
                
                match token:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num2 - num1
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = int(num2 / num1)
                        # if num2 / num1 < 0:
                        #     result = math.ceil(num2 / num1)
                        # else:
                        #     result = math.floor(num2 / num1)
                        #print(" => ", result)
                
                stk1.append(result)
            #print(token, stk1)
        return stk1.pop()
    
sol1 = Solution()
#print(sol1.evalRPN(["2","1","+","3","*"]))
# print(sol1.evalRPN(["4","13","5","/","+"]))
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol1.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

                
