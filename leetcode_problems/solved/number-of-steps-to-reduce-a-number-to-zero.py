class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num!=0:
            if num%2==0:
                num = int(num/2)
            else:
                num -= 1
            steps += 1
            print(num)
        return steps
    
sol1 = Solution()
print(sol1.numberOfSteps(5))
#O(logn)
