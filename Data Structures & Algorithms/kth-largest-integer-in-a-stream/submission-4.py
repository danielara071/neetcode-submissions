class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.heap_size = k
        for i in range(len(nums)):
            if len(self.h) >= self.heap_size:
                heapq.heappushpop(self.h, nums[i])
            else:
                heapq.heappush(self.h, nums[i])

    def add(self, val: int) -> int:
        if len(self.h) >= self.heap_size:
            heapq.heappushpop(self.h, val)
        else:
            heapq.heappush(self.h, val)
        return self.h[0]
