class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n -1 
        while left <= right:
            m  = left + ((right - left) //2 )
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return -1