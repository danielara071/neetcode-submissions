class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neww = [0] * (2 * n)
        res = []

        for i in range(n):
            j = -i - 1
            neww[i] = nums[i]
            neww[j] = nums[j]
        return neww
        
        