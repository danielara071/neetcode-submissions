class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            sett = set()
            for j in range(9):
                item = board[i][j]
                if item in sett:
                    return False
                elif item != ".":
                    sett.add(item)
        for i in range(9):
            sett = set()
            for j in range(9):
                item = board[j][i]
                if item in sett:
                    return False
                elif item != ".":
                    sett.add(item)
        starts= [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3),(6,6) ]

        for i,j in starts:
            sett = set()
            for row in range(i, i +3):
                for col in range(j, j +3):
                    item = board[row][col]
                    if item in sett:
                        return False
                    elif item != ".":
                        sett.add(item)
        return True

