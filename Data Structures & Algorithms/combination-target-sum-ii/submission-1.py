class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            elif total > target or i >= n:
                return

            arr.append(candidates[i])
            backtrack(i+ 1, arr, total + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i+ 1]:
                i += 1
            arr.pop()
            backtrack(i + 1, arr, total)
        backtrack(0,[],0)
        return res