#https://leetcode.com/problems/sum-multiples/description/

# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive 
# that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for num in range(1, n+1):
            if num%3==0 or num%5==0 or num%7==0:
                total += num
        return total
    
sol1 = Solution()
print(sol1.sumOfMultiples(7))
print(sol1.sumOfMultiples(10))
print(sol1.sumOfMultiples(9))
        
#time - O(n)
#space - O(1)