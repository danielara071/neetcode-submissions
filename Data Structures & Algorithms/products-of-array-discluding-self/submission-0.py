class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        lmult = [0] * n
        rmult = [0] * n 
        for i in range(n):
            j = -i - 1
            lmult[i] = left
            rmult[j] = right
            left *= nums[i]
            right *= nums[j]
        
        return [l *r for l, r in zip(lmult, rmult)]