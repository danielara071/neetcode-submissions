class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs =[]
        sol = []
        def backtrack(n):
            if n >= len(nums):
                sol.append(subs.copy())
                return
            subs.append(nums[n])
            backtrack(n +1 )
            subs.pop()
            backtrack(n + 1)
        backtrack(0)
        return sol
