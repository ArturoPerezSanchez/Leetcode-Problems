# https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        stack = deque()
        counter = 0
        for row in range(m):
            for col in range(n):
                val = grid[row][col]
                if (val == 1): counter +=1
                elif (val == 2): stack.append((row, col))

        res = -int(len(stack) != 0)
        
        while(stack):
            
            res+=1
            for i in stack:
                x, y = i
                grid[x][y] = 2

            for i in range(len(stack)):
                x, y = stack.popleft()
                if(x > 0 and grid[x-1][y] == 1): 
                    grid[x-1][y] = 2
                    stack.append((x-1, y))
                if(x < m-1 and grid[x+1][y] == 1): 
                    grid[x+1][y] = 2
                    stack.append((x+1, y))
                if(y > 0 and grid[x][y-1] == 1): 
                    grid[x][y-1] = 2
                    stack.append((x, y-1))
                if(y < n-1 and grid[x][y+1] == 1): 
                    grid[x][y+1] = 2
                    stack.append((x, y+1))
            counter -=len(stack)
        return res if(counter == 0) else -1