class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        n = len(s)
        left = 0  
        longest = 0
        for i in range(n):
            while s[i] in sett:
                sett.remove(s[left])
                left += 1
            window = i - left + 1
            longest = max(window, longest)
            sett.add(s[i])
        return longest
