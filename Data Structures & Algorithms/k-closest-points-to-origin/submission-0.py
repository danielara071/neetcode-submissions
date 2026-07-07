class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        origin = [0,0]
        for x, y in points:
            distance = math.sqrt((x - origin[0])**2 + (y - origin[0])**2)
            point = (-distance, [x, y])
            if len(heap) >= k:
                heapq.heappushpop(heap, point)
            else:
                heapq.heappush(heap, point)
        return [h for d, h in heap]