class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for num in nums:
            length = 0
            if num - 1 in sett:
                continue
            while num in sett:
                length += 1
                longest = max(length, longest)
                num +=1 
        return longest
