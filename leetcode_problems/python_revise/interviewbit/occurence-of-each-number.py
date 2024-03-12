#https://www.interviewbit.com/problems/occurence-of-each-number/

# You are given an integer array A.

# You have to find the number of occurences of each number.

# Return an array containing only the occurences with the smallest value's occurence first.

# For example, A = [4, 3, 3], you have to return an array [2, 1], where 2 is the number of occurences for element 3, 
# and 1 is the number of occurences for element 4. But, 2 comes first because 3 is smaller than 4.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        
        numMap = {}
        for num in A:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        keys = list(numMap.keys())
        keys.sort()
        result = []
        for key in keys:
            result.append(numMap[key])
        
        return result

sol1 = Solution()
print(sol1.findOccurences([4, 3, 3]))