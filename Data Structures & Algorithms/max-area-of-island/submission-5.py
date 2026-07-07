class Solution:
    def __init__(self):
        self.max_area = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1, 0), (-1,0), (0, 1), (0, -1)]
        visited = set()
        def bfs(start):
            area = 1
            q = collections.deque([start])
            visited.add(start)
            while q:
                i, j = q.popleft()
                for x, y in dirs:
                    r = x + i
                    c = y + j
                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or (r, c) in visited:
                        continue
                    visited.add((r, c))
                    q.append((r, c))
                    area +=1 
            self.max_area = max(self.max_area, area)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs((i, j))
                    visited.add((i, j))
        return self.max_area