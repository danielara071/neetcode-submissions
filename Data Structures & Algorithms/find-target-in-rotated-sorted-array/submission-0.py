class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = n -1
        while left < right:
            m = left + ((right - left)// 2)
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        mini = left
        if mini == 0:
            left = 0
            right = n - 1
        elif target >= nums[0] and target <= nums[mini -1]:
            left = 0
            right = mini - 1
        else:
            left = mini
            right = n - 1
        while left <= right:
            m = left + ((right - left)//2 )
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return -1