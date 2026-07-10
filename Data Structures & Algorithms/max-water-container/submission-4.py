class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        n = len(heights)
        right = n - 1
        while left < right:
            d = right - left 
            area = min(heights[left], heights[right]) * d
            max_water = max(max_water, area)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return max_water