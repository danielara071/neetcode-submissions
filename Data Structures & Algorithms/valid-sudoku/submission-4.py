class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = 9
        c = 9
        for i in range(r):
            seen = set()
            for j in range(c):
                box = board[i][j]
                if box in seen:
                    return False
                elif box != ".":
                    seen.add(box)
        for i in range(r):
            seen = set()
            for j in range(c):
                box = board[j][i]
                if box in seen:
                    return False
                elif box != ".":
                    seen.add(box)

        grid = [(0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6)]

        for i, j in grid:
            seen = set()
            for row in range(i, i+3 ):
                for col in range(j, j+ 3):
                    box = board[row][col]
                    if box in seen:
                        return False
                    elif box != ".":
                        seen.add(box)
        return True


            