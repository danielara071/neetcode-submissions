class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        larr = [1] * n
        rarr = [1] * n
        left = 1
        right = 1 
        for i in range(n):
            j = -i -1
            larr[i] = left
            rarr[j] = right
            left *= nums[i]
            right *= nums[j]
        
        return [l* r for l, r in zip(larr, rarr)]
