class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        #heights=[2,1,5,6,2,3]
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                area = (i - idx) * height
                max_area = max(max_area, area)
                start = idx
            stack.append((start, h))

        for i , h in stack:
            area = h * (len(heights) - i)
            max_area = max(area, max_area)
        return max_area