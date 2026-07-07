class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(start):
            visited = set()
            q = collections.deque()
            distance = {}
            for item in start:
                visited.add(item)
                q.append(item)
                distance[item] = 0
            while q:
                i, j = q.popleft()
                for x, y in dirs:
                    r = x + i
                    c = y + j 
                    if r >= rows or r <0 or c < 0 or c >= cols or grid[r][c] == -1 or (r, c) in visited:
                        continue
                    distance[(r, c)] = distance[(i, j)] + 1
                    grid[r][c] = distance[(i, j)] + 1
                    q.append((r,c))
                    visited.add((r, c))


        chests = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    chests.append((i, j))
        
        bfs(chests)


