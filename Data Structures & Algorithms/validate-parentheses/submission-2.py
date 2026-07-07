class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        for p in s:
            if p in parentheses:
                if stack:
                    opening = stack.pop()
                    if parentheses[p] != opening:
                        return False
                else:
                    return False
            else:
                stack.append(p)
        if stack:
            return False
        return True
