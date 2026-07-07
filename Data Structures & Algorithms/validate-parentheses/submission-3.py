class Solution:
    def isValid(self, s: str) -> bool:
        #[
        dic = {"]" : "[", ")" : "(", "}" : "{"}
        stack = []
        for bracket in s:
            if bracket in dic:
                if stack:
                    popped = stack.pop()
                    if dic[bracket] != popped:
                        return False
                else:
                    return False

            else:
                stack.append(bracket)
        return not stack