from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iterations = len(nums) * k
        temp = nums[1]
        for i in range(iterations):
            nums[i+1] = nums[i]
            