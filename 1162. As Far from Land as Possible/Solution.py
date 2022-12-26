# https://leetcode.com/problems/as-far-from-land-as-possible

class Solution:
    # BFS solution
    def maxDistance(self, grid: List[List[int]]) -> int:
        stack = deque()
        ans = -1
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if(grid[i][j] == 1):
                    if(i>0   and grid[i-1][j] == 0): stack.append((i-1,j))
                    if(i<n-1 and grid[i+1][j] == 0): stack.append((i+1,j))
                    if(j>0   and grid[i][j-1] == 0): stack.append((i,j-1))
                    if(j<n-1 and grid[i][j+1] == 0): stack.append((i,j+1))
        while(stack):
            ans+=1
            for _ in range(len(stack)):
                i, j = stack.popleft()
                if(grid[i][j] == 0):
                    grid[i][j] = 1
                    if(i>0): stack.append((i-1,j))
                    if(j>0): stack.append((i,j-1))
                    if(i<n-1): stack.append((i+1,j))
                    if(j<n-1): stack.append((i,j+1))

        return ans



    # Brute force solution
    def maxDistance2(self, grid: List[List[int]]) -> int:
        global dMatrix
        n = len(grid)
        dMatrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(2*n)
            dMatrix.append(row)

        @cache
        def update(row, col, val):
            global dMatrix
            dMatrix[row][col] = val
            val +=1
            if(row>0   and dMatrix[row-1][col]>val): update(row-1, col, val)
            if(row<n-1 and dMatrix[row+1][col]>val): update(row+1, col, val)
            if(col>0   and dMatrix[row][col-1]>val): update(row, col-1, val)
            if(col<n-1 and dMatrix[row][col+1]>val): update(row, col+1, val)



        for row in range(n):
            for col in range(n):
                if(grid[row][col] == 1):
                    update(row, col, 0)
        ans = 0
        for row in dMatrix:
            for cell in row:
                ans = max(ans, cell)
        if(ans == 0 or ans == 2*n): return -1
        return ans