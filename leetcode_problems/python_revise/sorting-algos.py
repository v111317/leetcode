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
    
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j>0 and nums[j-1] > nums[j]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = temp
                j -= 1
        return nums        
                
        

sol1 = SortingAlgos()
print(sol1.selectionSort([1, 9, 4, 3, 8, 10, 2, 4]))
print(sol1.bubbleSort([1, 9, 4, 3, 8, 10, 2, 4]))
print(sol1.insertionSort([1, 9, 4, 3, 8, 10, 2, 4]))
             