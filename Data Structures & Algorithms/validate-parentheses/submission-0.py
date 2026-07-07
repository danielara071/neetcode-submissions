class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "}" : "{", "]" : "["}
        stack = []
        for bracket in s:
            if bracket in dic:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != dic[bracket]:
                    return False
            else:
                stack.append(bracket)
        
        return not stack