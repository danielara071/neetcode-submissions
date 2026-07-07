class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol =  []
        subs = []
        candidates.sort()
        def backtrack(i, summ):
            if summ == target:
                if subs not in sol:
                    sol.append(subs.copy())
                return
            if summ >= target or i >= len(candidates):
                return

            subs.append(candidates[i])
            backtrack(i + 1, summ + candidates[i])
            subs.pop()
            backtrack(i + 1, summ)

        backtrack(0,0)
        return sol