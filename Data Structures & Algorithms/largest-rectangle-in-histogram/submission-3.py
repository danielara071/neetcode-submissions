class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                maxArea = max(maxArea, area)
                start = index
            stack.append((start, h))
        
        for i , h in stack:
            area = (len(heights) - i) * h
            maxArea = max(maxArea, area)
        return maxArea


"""
Push when heights increase.

When height drops, pop and compute areas.

The drop tells you exactly where tall bars must stop.
"""