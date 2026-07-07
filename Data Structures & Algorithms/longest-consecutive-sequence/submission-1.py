class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxi = 0
        for n in nums:
            if n - 1 not in sett:
                curr = n
                longest = 1
                while curr in sett:
                    maxi = max(maxi, longest)
                    curr += 1
                    longest += 1
        return maxi 
