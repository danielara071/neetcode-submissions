class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        rows = len(board)
        cols = len(board[0])
        def dfs(start):
            visited = set(start)
            stack = [start]
            board[start[0]][start[1]] = "T"

            while stack:
                i, j = stack.pop()
                for x, y in dirs:
                    r = x +i
                    c = y +j
                    if r < 0 or c  <0 or r >= rows or c >= cols or board[r][c] == "X" or (r, c) in visited:
                        continue
                    visited.add((r, c))
                    stack.append((r, c))
                    board[r][c] = "T"
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs((r, 0))
            if board[r][cols- 1] == "O":
                dfs((r, cols-1))

        for c in range(cols):
            if board[0][c] == "O":
                dfs((0, c))
            if board[rows- 1][c] == "O":
                dfs((rows - 1, c))
        

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
    



