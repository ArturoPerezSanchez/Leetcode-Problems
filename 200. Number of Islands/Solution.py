# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def floodfill(row,col):
                if(row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and grid[row][col] == "1"):
                    grid[row][col] = 0
                    floodfill(row-1,col)
                    floodfill(row+1, col)
                    floodfill(row,col-1)
                    floodfill(row, col+1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    res+=1
                    floodfill(i,j)
        return res