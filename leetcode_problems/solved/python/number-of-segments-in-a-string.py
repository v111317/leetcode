class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        count = 0

        for w in words:
            if len(w) != 0:
                count += 1
                
        if len(s)==0:
            return 0
        else:
            return count
    
    
sol1 = Solution()
print(sol1.countSegments("Hello, my name is John"))
print(sol1.countSegments("Hello"))
print(sol1.countSegments("      "))
print(sol1.countSegments(", , , ,        a, eaefa"))

#time - O(n)
#space - O(1)