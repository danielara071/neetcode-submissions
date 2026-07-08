class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for char in s:
            if char in pairs:
                if not stack:
                    return False
                popped = stack.pop()
                if pairs[char] != popped:
                    return False
            else:
                stack.append(char)
        return not stack
                
# stack = ["(", "{"]