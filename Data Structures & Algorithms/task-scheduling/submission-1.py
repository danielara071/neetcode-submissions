class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = Counter(tasks)
        heap = []
        for k, v in task_frequency.items():
            heapq.heappush(heap, -v)
        
        q = collections.deque()
        time = 0
        while q or heap:
            time += 1
            if heap:
                task_count = heapq.heappop(heap)
                task_count += 1
                if task_count < 0:
                    q.append((time + n, task_count))
            if q:
                if q[0][0] == time:
                    heapq.heappush(heap, q.popleft()[1])
        return time
