#https://leetcode.com/problems/jewels-and-stones/description/

# You're given strings jewels representing the types of stones that are jewels, and stones 
# representing the stones you have. Each character in stones is a type of stone you have. 
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        
        return count

sol1 = Solution()
print(sol1.numJewelsInStones("aA", "aAAbbbb"))
print(sol1.numJewelsInStones("z", "ZZ"))