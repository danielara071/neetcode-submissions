class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        q = collections.deque()
        order = []
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            order.append(node)
        if len(order) != numCourses:
            return False
        return True

    

