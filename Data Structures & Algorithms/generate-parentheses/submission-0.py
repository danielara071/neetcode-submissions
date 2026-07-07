class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        res = []
        def backtrack(opened, closed):
            if 2*n == len(sol):
                res.append("".join(sol))
                return

            if opened < n:
                sol.append("(")
                backtrack(opened + 1, closed)
                sol.pop()
            
            if opened > closed:
                sol.append(")")
                backtrack(opened, closed+ 1)
                sol.pop()
        backtrack(0,0)
        return res