class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1, 0], [-1, 0] , [0, 1], [0 ,-1]]
        m = len(grid)
        n = len(grid[0])
        maxarea = 0
        #dfs 
            #check if the position is valid 

            #extend max area
            #check neighbors
                #dfs

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            area = 1
            for row , col in directions:
                area += dfs(r + row, c + col)
            return area
        #iterate trhough the matrix 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r, c))
        return maxarea

