# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution:
    '''
    Time complexity: O(m*n), The function loops through each element in the grid once, so the time complexity of this function is O(m*n),
                 where m is the number of rows in the grid and n is the number of columns in the grid.


    Space complexity: O(n), To keep track of the maximum length of integers in each column, the function uses a list of length equal to the number of columns in the grid.
    '''
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        # Create a list of zeros with length equal to the number of columns in the grid.
        res = [0]*len(grid[0])
        
        # Loop through the rows and columns of the grid.
        # For each column, update the value in the res list to be the maximum length of the integer in that column.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res[c] = max(res[c], len(str(grid[r][c])))
        
        # Return the res list containing the maximum length of integers for each column of the grid.
        return res