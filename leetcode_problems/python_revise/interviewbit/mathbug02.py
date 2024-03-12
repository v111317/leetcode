class Solution:
	# @param A : integer
	# @return a list of list of integers
    def squareSum(self, A):
        ans = set()
        a = 0
        while a * a < A:
            b = 0
            while b * b < A:
                if a * a + b * b == A:
                    newEntry = [a, b]
                    newEntry.sort()
                    newEntry = tuple(newEntry)
                    ans.add(newEntry)
                b += 1
            a += 1
        result = []
        for t in ans:
            result.append(list(t))
        return result

sol1 = Solution()
for i in range(5,6):
    print(i, sol1.squareSum(i))