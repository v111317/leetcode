#https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string 
# is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketMap = ["()", "[]", "{}"]
        
        if len(s)%2 == 1:
            return False
        
        bracketStack = []
        
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                bracketStack.append(bracket)
            else:
                bracketOut = bracketStack.pop() if len(bracketStack)>0  else ""
                if bracketOut+bracket not in bracketMap:
                    return False
                
        if len(bracketStack) != 0:
            return False
        
        return True
    
sol1 = Solution()
#print(sol1.isValid("()[}"))
print(sol1.isValid("}("))

#time - O(n)
#space - O(n) incase all brackets are like ((((