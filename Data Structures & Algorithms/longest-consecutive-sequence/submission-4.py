class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for num in sett:
            if num - 1 not in sett:
                start = num 
                current = 0
                while start in sett:
                    current += 1
                    longest = max(longest, current)
                    start += 1

        return longest

# [1,2,3,4,5]