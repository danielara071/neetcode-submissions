class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for n in sett:
            if n - 1 not in sett:
                nextnum = n + 1
                length = 1
                while nextnum in sett:
                    nextnum += 1
                    length += 1
                longest = max(longest, length)
        return longest