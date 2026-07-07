class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        for key, val in count.items():
            if len(heap) >= k:
                heapq.heappushpop(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [v for k, v in heap]