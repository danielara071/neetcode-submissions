class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        n = len(heights)
        left = 0
        right = n - 1
        while left < right:
            w = right - left 
            h = min(heights[left], heights[right])
            a = w * h
            maxarea = max(a, maxarea)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxarea