# https://leetcode.com/problems/sudoku-solver


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def getPossibles(board, row, col):
            nums = ["1","2","3","4","5","6","7","8","9"]
            # Borramos los numeros ocupados en esa fila y columna
            for i in range(9):
                if board[row][i] in nums:
                    nums.remove(board[row][i])
                if board[i][col] in nums:
                    nums.remove(board[i][col])
            
            #Borramos los numeros ya ocupados en ese cuadrante
            qr = (row//3)
            qc = (col//3)
            for i in range(qr*3, qr*3+3):
                for j in range(qc*3, qc*3+3):
                    if(board[i][j] in nums):
                        nums.remove(board[i][j])
            return nums
        
        def baktracking(board):
            nums = []
            completed = True
            # Buscamos la casilla con menor número de opciones posibles
            min_options = 10
            min_row = 0
            min_col = 0
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        options = getPossibles(board, i, j)
                        if len(options) < min_options:
                            min_options = len(options)
                            min_row = i
                            min_col = j
            # Si no hay casillas vacías, hemos encontrado la solución
            if min_options == 10:
                return True
            # Realizamos la llamada recursiva con todos los números disponibles para la casilla con menor número de opciones
            for i in getPossibles(board, min_row, min_col):
                board[min_row][min_col] = i
                # Si es valido devolvemos True, si no probamos con el siguiente numero
                if baktracking(board):
                    return True
            # Si hemos llegado a este punto, es porque ningún número era válido para la casilla con menor número de opciones, 
            # por lo que devolvemos False para cortar la rama del árbol de búsqueda
            board[min_row][min_col] = "."
            return False

        baktracking(board)

