class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sizeA = len(A)
        windowLen = B
        
        maxSum = 0
        print(sizeA)
        for i in range(3, 52):
            maxSum += A[i]
            
        C = []
        C.append([0]*4)
        print(C)
        print(maxSum)
        return
        for i in range(sizeA-windowLen, sizeA+windowLen):
            sumNums = 0
            k = i
            for j in range(0, windowLen):
                sumNums += A[k%sizeA]
                k += 1
            print(i, sumNums)
            if sumNums==8067:
                break
            maxSum = max(sumNums, maxSum)
        return maxSum

sol1 = Solution()
#print(sol1.solve([5, -2, 3 , 1, 2], 3)) 
#print(sol1.solve([1, 2], 1)) 
list1 = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]


    
print(sol1.solve(list1, 48))
