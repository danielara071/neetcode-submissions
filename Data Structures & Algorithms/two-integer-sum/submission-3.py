class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {}
        for i in range(n):
            h[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in h and h[complement] != i:
                return [i, h[complement]]
