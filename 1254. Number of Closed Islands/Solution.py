# https://leetcode.com/problems/number-of-closed-islands

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def floodfill(row,col):
            if   row==0 or row==len(grid)   -1: aux = True
            elif col==0 or col==len(grid[0])-1: aux = True
            else: aux = False

            grid[row][col] = 1
            if(row > 0              and not grid[row-1][col]): aux += floodfill(row-1,col)
            if(row < len(grid)-1    and not grid[row+1][col]): aux += floodfill(row+1, col)
            if(col > 0              and not grid[row][col-1]): aux += floodfill(row,col-1)
            if(col < len(grid[0])-1 and not grid[row][col+1]): aux += floodfill(row, col+1)
            return aux

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not (grid[i][j] or floodfill(i,j)): res+=1

        return res