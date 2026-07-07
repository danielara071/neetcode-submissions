class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    #move up/down row same column, move left/right column same row
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(r, c):
            if r >=m or r < 0 or c < 0 or c >= n or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for row, col in directions:
                dfs(r + row, c + col )


        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands +=1

        return islands

