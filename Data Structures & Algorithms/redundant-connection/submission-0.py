class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = max(max(x, y) for x, y in edges)
        parent = [i for i in range(nodes + 1)]
        size = [1] * (nodes + 1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            a = find(x)
            b = find(y)
            if a == b:
                return False
            
            if size[a] > size[b]:
                parent[b] = a
                size[a] += size[b]
            else:
                parent[a] = b
                size[b] += size[a]

            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]
