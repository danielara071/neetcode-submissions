class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        dirs = [(1,0), (-1,0), (0, -1), (0, 1)]
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        def bfs(start):
            q = collections.deque()
            q.append(start)
            visited.add(start)
            while q:
                i , j = q.popleft()
                for x , y in dirs:
                    new_row = x + i
                    new_col = y + j
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] == "0" or (new_row, new_col) in visited:
                        continue
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    bfs((i, j))
        return islands