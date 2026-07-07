class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kworks(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p /k)
            return hours <= h
        
        left = 1
        right = max(piles)
        while left < right:
            m = left + ((right-left)//2)
            if kworks(m):
                right = m
            else:
                left = m + 1
        return left