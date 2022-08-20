# https://leetcode.com/problems/number-of-islands-ii

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if(m == 1 and n == 1): return [0] if len(positions) == 0 else [1]
        noIslands = 0
        res = []
        grid = [[0 for i in range (n)] for j in range (m)]

        def getAdj(row, col):
            adj = set()
            if (row != 0): adj.add((grid[row-1][col], row-1, col))
            if (col != 0): adj.add((grid[row][col-1], row, col-1))
            if (row != m-1): adj.add((grid[row+1][col], row+1, col))
            if (col != n-1): adj.add((grid[row][col+1], row, col+1))
            return sorted(adj)
        
        def expand(oldVal, newVal, row, col):
            grid[row][col] = newVal
            if (row != 0 and grid[row-1][col] == oldVal): expand(oldVal, newVal, row-1, col)
            if (col != 0 and grid[row][col-1] == oldVal): expand(oldVal, newVal, row, col-1)
            if (row != m-1 and grid[row+1][col] == oldVal): expand(oldVal, newVal, row+1, col)
            if (col != n-1 and grid[row][col+1] == oldVal): expand(oldVal, newVal, row, col+1)
        
        currentPosition = 0
       
        for i in positions:
            currentPosition +=1
            row, col = i
            
            if(grid[row][col] != 0): 
                res.append(noIslands)
                continue
            adjacentIslands = getAdj(row, col)
            differentIslands = set()

            for i in adjacentIslands: differentIslands.add(i[0])
            differentIslands = sorted(differentIslands)
            if(len(differentIslands) == 1):
                # New Island
                if(differentIslands[0] == 0):
                    grid[row][col] = currentPosition
                    noIslands +=1
                # Expanding existing Island
                else: grid[row][col] = differentIslands[0]

            else:
                mergeVal = adjacentIslands[-1][0]
                grid[row][col] = mergeVal
                changedIslands = []
                for i in adjacentIslands:
                    curVal, curRow, curCol = i
                    if(curVal != 0 and curVal != mergeVal):
                        if(curVal not in changedIslands):
                            noIslands -=1
                            changedIslands.append(curVal)
                        expand(curVal, mergeVal, curRow, curCol)
            res.append(noIslands)

        return res

                    










