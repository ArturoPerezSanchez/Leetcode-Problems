# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = 0
        for row in board:
            aux = []
            for el in row:
                if(el != "." and el in aux):
                    return False
                else:
                    aux.append(el)
            
            aux = []
            for r in range(9):
                el = board[r][col]
                if(el != "." and el in aux):
                    return False
                else:
                    aux.append(el)
            col+=1
        
        col = 0
        for row in range (0, 9, 3):
            for col in range(0, 9, 3):
                aux = []
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        el = board[i][j]
                        if(el != "." and el in aux):
                            return False
                        else:
                            aux.append(el)
        return True
                        
                        
                        
                        
                        
                        
                        
                