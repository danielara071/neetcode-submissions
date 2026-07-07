class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for num in nums:
            length = 0
            if num - 1 not in sett:
                while num in sett:
                    length +=1 
                    num +=1 
            longest = max(longest, length)
        return longest
    # [1,2,3,6,7,9]
            

