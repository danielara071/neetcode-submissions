class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            dic[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in dic and dic[complement] != i:
                return [i, dic[complement]]