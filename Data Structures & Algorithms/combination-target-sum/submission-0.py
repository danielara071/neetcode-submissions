class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []

        def backtrack(i, curr, summ):
            if summ == target:
                sol.append(curr.copy())
                return
            if i >= len(nums) or summ > target:
                return
            
            curr.append(nums[i])
            backtrack(i, curr, summ + nums[i])
            curr.pop()
            backtrack(i + 1, curr, summ)

        backtrack(0, [], 0)
        return sol

            