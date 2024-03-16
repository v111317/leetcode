#selection sort     - find the min 
#bubble sort        - swap neighbors until end of array
#insertion sort     - pick element and swap till element in place

class SortingAlgos:
    
    def selectionSort(self, nums):
        if len(nums)==1:
            return nums
        
        i = 0
        for i in range(len(nums)):
            # minNum = nums[i]
            minNumIdx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minNumIdx]:
                #    minNum = nums[j]
                   minNumIdx = j
            if minNumIdx!=i:
                temp = nums[i]
                nums[i] = nums[minNumIdx]
                nums[minNumIdx] = temp
        
        return nums
    
    def bubbleSort(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums
    
    # it fixes a position and works to sort all elements upto the fixed position
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j>0 and nums[j-1] > nums[j]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                j -= 1
        return nums
    
    def mergeSort(self, nums):
        if len(nums) in [0, 1]:
            return nums
        else:
            #print(nums)
            mid = len(nums)//2
            
            leftArr =  []
            for i in range(0, mid):
                leftArr.append(nums[i])
            
            rightArr = []
            for i in range(mid, len(nums)):
                rightArr.append(nums[i])
            
            #print(" => ", leftArr)
            #print(" => ", rightArr)    
            leftArr = self.mergeSort(leftArr)
            rightArr = self.mergeSort(rightArr)   
            
            result = []
            i = 0
            j = 0
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] < rightArr[j]:
                    result.append(leftArr[i])
                    i += 1
                else:
                    result.append(rightArr[j])
                    j += 1
            
            while i < len(leftArr):
                result.append(leftArr[i])
                i += 1
                
            while j < len(rightArr):
                result.append(rightArr[j])    
                j += 1
            #print(" ===> ", result)
            return result
    
    def quickSort(self, nums, start, end):
        # print(start, end)
        # if start==0 and end==5:
        #     exit()
        if start>=end:
            return
        
        #pivot = nums[end]
        pIdx = self.partition(nums, start, end)
        # print(" => ", pIdx)
        self.quickSort(nums, start, pIdx-1)
        self.quickSort(nums, pIdx+1, end)
        
        return 
    
    
    def partition(self, nums, start, end):
        #a = 1
        pivot = nums[end]
        pIdx = start
        for i in range(start, end):
            # print(nums, pIdx)
            if nums[i] <= pivot:
                temp = nums[i]
                nums[i] = nums[pIdx]
                nums[pIdx] = temp
                pIdx += 1     
        temp = nums[pIdx]
        nums[pIdx] = nums[end]
        nums[end] = temp
        # print(nums)
        return pIdx

sol1 = SortingAlgos()
# print(sol1.selectionSort([1, 9, 4, 3, 8, 10, 2, 4]))
# print(sol1.bubbleSort([1, 9, 4, 3, 8, 10, 2, 4]))
#print(sol1.insertionSort([1, 9, 4, 3, 8, 10, 2, 4]))
#print(sol1.mergeSort([1, 9, 4, 3, 8, 10, 2, 4]))
nums = [1, 9, 4, 3, 8, 10, 2, 4]
sol1.quickSort(nums, 0, 7)
print(nums)

             