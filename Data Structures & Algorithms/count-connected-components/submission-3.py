class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = collections.defaultdict(list)
        components = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(start):
            visited.add(start)
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)


        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components
        

        