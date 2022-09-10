# https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        def rec(row, col):
            if((row, col) in visited): return 0
            if(row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0): return 0
            visited.add((row, col))
            return 1 + rec(row+1, col) + rec(row-1, col) + rec(row, col+1) + rec(row, col-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == 1):
                    res = max(res, rec(r,c))
        
        return res
