class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set(nums)
        return not len(sett) == len(nums)