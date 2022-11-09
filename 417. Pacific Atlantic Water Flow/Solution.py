# https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        visited = set()
        res = set()
        def rec1 (i,j):
            visited.add((i,j))
            atlantic.add((i,j))

            if(j<len(heights[0])-1 and (i == 0 or heights[i][j+1] >= heights[i][j])) and (i,j+1) not in visited:  rec1(i, j+1)
            if(j>0 and (i == 0 or heights[i][j-1] >= heights[i][j])) and (i,j-1) not in visited: rec1(i, j-1)
            if(i<len(heights)-1 and (j == 0 or heights[i+1][j] >= heights[i][j])) and (i+1,j) not in visited: rec1(i+1, j)
            if(i>0 and (j == 0 or heights[i-1][j] >= heights[i][j])) and (i-1,j) not in visited: rec1(i-1, j)

        def rec2 (i,j):
            visited.add((i,j))
            if((i,j) in atlantic): res.add((i,j))

            if(j<len(heights[0])-1 and (i == len(heights)-1 or heights[i][j+1] >= heights[i][j])) and (i,j+1) not in visited: rec2(i, j+1)
            if(j>0 and (i == len(heights)-1 or heights[i][j-1] >= heights[i][j])) and (i,j-1) not in visited: rec2(i, j-1)
            if(i<len(heights)-1 and (j == len(heights[0])-1 or heights[i+1][j] >= heights[i][j])) and (i+1,j) not in visited: rec2(i+1, j)
            if(i>0 and (j == len(heights[0])-1 or heights[i-1][j] >= heights[i][j])) and (i-1,j) not in visited: rec2(i-1, j)

        rec1 (0,0)
        visited = set()
        rec2 (len(heights)-1,len(heights[0])-1)
        

        return res

