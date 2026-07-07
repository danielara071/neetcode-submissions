class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right =0
        n = len(height)
        lwall = [0] * n
        rwall = [0] * n
        for i in range(n):
            j = -i -1 
            lwall[i] = left
            rwall[j] = right
            left = max(height[i], left)
            right = max(height[j], right)

        summ = 0
        for i in range(n):
            pot = min(lwall[i], rwall[i])
            summ += max(0, pot - height[i])
        return summ