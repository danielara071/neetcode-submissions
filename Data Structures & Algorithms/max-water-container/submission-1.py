class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            b = right - left 
            h = min(heights[left], heights[right])
            area = b * h
            max_area = max(max_area, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left +=1 
        return max_area
            