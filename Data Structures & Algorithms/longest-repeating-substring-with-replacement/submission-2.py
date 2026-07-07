class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        longest = 0
        left = 0
        n = len(s)
        for right in range(n):
            count[ord(s[right]) - ord("A")] += 1
            window = right - left + 1
            while window - max(count) > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1
                window = right - left +1 
            longest = max(longest, window)
        return longest
