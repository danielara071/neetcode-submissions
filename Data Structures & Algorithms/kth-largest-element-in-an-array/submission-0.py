class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        kth = 0
        for i in range(k):
            kth = heapq.heappop(nums)
        return -kth