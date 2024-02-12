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