import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        left = 0 
        right = len(s) - 1  
        while left <= right:
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1
        return True
