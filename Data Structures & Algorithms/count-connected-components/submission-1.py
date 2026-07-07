class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        dic = defaultdict(list)
        visited = set()
        for u, v in edges:
            dic[u].append(v)
            dic[v].append(u)

        def dfs(start):
            stack = deque()
            stack.append(start)
            order = []
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    order.append(node)
                    for nei in dic[node]:
                        stack.append(nei)
            return order

        for node in range(n):
            if node not in visited:
                v = dfs(node)
                for nei in v:
                    visited.add(nei)
                count += 1
        return count
