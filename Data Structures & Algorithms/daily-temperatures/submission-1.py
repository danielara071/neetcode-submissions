class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([i, t])
        return res

        #stack = [(0, 30), ]
        #stack = [(0, 38), (2, 30)]
        #stack = [(0, 38), (3, 36)]
        #stack = [(0, 38), (3, 36), (4, 35)]
        #stack = [(0, 38), (3, 36), (4, 35)]