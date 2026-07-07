class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()
        n = len(s)
        m = 0
        for right in range(n):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            window = right -left +1
            m = max(window, m)
            sett.add(s[right])
        return m