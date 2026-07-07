class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n - 1
        while left < right:
            m = left + ((right-left)//2)
            if nums[m] > nums[right]:
                left = m + 1
            else:
               right = m
        return nums[left]