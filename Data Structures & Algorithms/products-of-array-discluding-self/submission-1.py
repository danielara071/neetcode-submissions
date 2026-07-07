class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lmult = [0]* n
        rmult = [0]* n
        l = 1
        r = 1
        for i in range(n):
            j = -i - 1
            lmult[i] = l
            rmult[j] = r
            l *= nums[i]
            r *= nums[j]
        
        return [l*r for l, r in zip(lmult, rmult)]