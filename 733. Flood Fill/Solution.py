# https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        global d
        d = {}
        
        def rec(row,col,newColor, oldColor):
            if((row,col) not in d):
                d[(row,col)] = True
                if(row>=0 and col>=0 and row<len(image) and col<len(image[0]) and image[row][col] == oldColor):
                    image[row][col] = newColor
                    rec(row-1,col,newColor,oldColor)
                    rec(row+1, col, newColor, oldColor)
                    rec(row,col-1,newColor,oldColor)
                    rec(row, col+1, newColor, oldColor)

        rec(sr,sc,color,image[sr][sc])
        return image