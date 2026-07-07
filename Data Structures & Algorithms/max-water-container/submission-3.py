class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            h = min(heights[left], heights[right])
            b = right - left 
            area = b * h
            max_area = max(area, max_area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area