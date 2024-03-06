#https://leetcode.com/problems/k-th-symbol-in-grammar/description/

# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. 
# Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, 
# and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

class Solution:
    #memory limit exceeded
    def kthGrammar(self, n: int, k: int) -> int:
        arr = "01"
        if n==1:
            return 0
        if n==2:
            return int("01"[k-1])
        
        for i in range(2, n):
            str1 = arr[0:len(arr)//2]
            str2 = arr[len(arr)//2:len(arr)]
                    
            arr = str1 + str2 + str2 + str1
        #print(arr)
        return int(arr[k-1])

sol1 = Solution()
#print(sol1.kthGrammar(1, 1))
# print(sol1.kthGrammar(2, 2))
# print(sol1.kthGrammar(5, 4))
print(sol1.kthGrammar(30, 434991989))
