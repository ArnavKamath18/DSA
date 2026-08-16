class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = []
            for val in row:
                if val.isnumeric():
                    if val in seen:
                        return False
                    seen.append(val)
        
        for i in range(9):
            seen = []
            for j in range(9):
                if board[j][i].isnumeric():
                        if board[j][i] in seen:
                            return False
                        seen.append(board[j][i])
        
        starts = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for i, j  in starts:
            if checkBox(i,j,board)==False:
                return False
        
        return True
        

def checkBox(i, j, board):
    seen = []
    for x in range(i,i+3):
        for y in range(j,j+3):
            if board[x][y].isnumeric():
                if board[x][y] in seen:
                    return False
                seen.append(board[x][y])