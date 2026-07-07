class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        fresh_fruits = 0
        def bfs(start, f):
            if f == 0:
                return 0
            visited = set()
            q = collections.deque()
            minutes = 0
            for item in start:
                visited.add(item)
                q.append(item)
            while q:
                changed = False
                for _ in range(len(q)):
                    i, j  = q.popleft()
                    for x, y in dirs:
                        new_row = x + i
                        new_col = y + j
                        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] == 0 or (new_row, new_col) in visited:
                            continue
                        f -= 1
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        changed = True
                if changed:
                    minutes += 1
            if f > 0:
                return -1
            return minutes

        sources = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    sources.append((i, j))
                if grid[i][j] == 1:
                    fresh_fruits += 1
        return bfs(sources, fresh_fruits)