
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        counter = Counter(nums)
        for key, val in counter.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))

        return [val for key, val in heap]

      