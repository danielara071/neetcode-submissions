class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = []
        for value in counter.values():
            heapq.heappush(heap, -value)
        q = collections.deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task < 0:
                    q.append((task, time + n))
            if q:

                if q[0][1] == time:
                    heapq.heappush(heap, q.popleft()[0])
        
        return time