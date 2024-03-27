from typing import List

#https://leetcode.com/problems/fizz-buzz/description/

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resultList = []
        for i in range(1, n+1):
            if i%15 == 0:
                resultList.append("FizzBuzz")
            elif i%3 == 0:
                resultList.append("Fizz")
            elif i%5 == 0:
                resultList.append("Buzz")
            else:
                resultList.append(str(i))
        return resultList
    
sol1 = Solution()
print(sol1.fizzBuzz(5))

#time - O(n)
#space - O(n)