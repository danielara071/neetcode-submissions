class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            a = find(x)
            b = find(y)
            if a == b:
                return 0
            if size[a] > size[b]:
                parent[b] = a
                size[a] += size[b]
            else:
                parent[a] = b
                size[b] += size[a]
            return 1
        for x, y in edges:
            n -= union(x, y)
        return n