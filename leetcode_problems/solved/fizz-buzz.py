from typing import List

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