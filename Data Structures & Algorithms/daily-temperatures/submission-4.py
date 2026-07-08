class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = []
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                t, idx = stack.pop()
                results[idx] = i - idx
            stack.append((temperatures[i], i))
        return results 




# stack = [30, 38]
