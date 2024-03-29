from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        if len(s)==1:
            return [0]
        A = s
        lastSeenXIdx = -1
        xArr = []
        
        for i in range(len(A)):
            if A[i]==c:
                lastSeenXIdx = i
            
            if lastSeenXIdx > -1:
                xArr.append(abs(i-lastSeenXIdx))
            else:
                xArr.append(-1)
        
        lastSeenXIdx = -1
        for i in range(len(A)-1,-1,-1):
            if A[i]==c:
                lastSeenXIdx = i
            
            if lastSeenXIdx > -1:
                if xArr[i]==-1:
                    xArr[i] = abs(i-lastSeenXIdx)
                else:    
                    xArr[i] = min(abs(i-lastSeenXIdx), xArr[i])
                        
        return xArr

sol1 = Solution()
print(sol1.shortestToChar("loveleetcode", 'e'))
print(sol1.shortestToChar("aaab", 'b'))
