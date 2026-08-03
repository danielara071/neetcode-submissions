class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for n in sett:
            if n - 1 not in sett:
                start = n
                length =  0
                while start in sett:
                    length += 1
                    longest = max(longest, length)
                    start += 1
        
        return longest
