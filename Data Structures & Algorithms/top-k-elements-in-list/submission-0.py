import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)
        for key, v in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(v, key))
            else:
                heapq.heappushpop(heap,(v,key))
        return [h[1] for h in heap]