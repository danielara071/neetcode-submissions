class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # if not prerequisites:
        #     return [0]
        adj = collections.defaultdict(list)
        order = []
        indegree = collections.defaultdict(int)
        q = collections.deque()
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
            return []
        return order
        
