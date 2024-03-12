#https://www.interviewbit.com/problems/count-element-occurence/

# Given a sorted array of integers, find the number of occurrences of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return 0

# **Example : **
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return 2.

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def findCount(self, A, B):
        start = 0
        end = len(A)-1
        mid = (start+end)//2
        
        if len(A)==1:
            if A[0]==B:
                return 1
            else:
                return 0
        
        idx = -1
        while start <= end:
            # print(start, end, mid)
            if A[mid]==B:
                idx = mid
                break
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start+end)//2
        
        if idx == -1:
            return 0
        count = 0
        i = idx
        while i>=0:
            if A[i]==B:
                count += 1
                i -= 1
            else:
                break
    
        i = idx + 1    
        while i < len(A):
            if A[i]==B:
                count += 1
                i += 1
            else:
                break
        return count

sol1 = Solution()
print(sol1.findCount([5, 7, 7, 8, 8, 10], 8))
print(sol1.findCount([1], 1))
print(sol1.findCount([ 1, 2, 6, 9, 9 ], 2))
