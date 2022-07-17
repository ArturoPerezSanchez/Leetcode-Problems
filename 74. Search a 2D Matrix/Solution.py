# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix)
        
        while(l<r):
            mid = (l+r)//2
            if(matrix[mid][0] <= target and matrix[mid][-1] >= target): break
            if(matrix[mid][0]>target): r = mid
            else: l = mid+1
        
        row = mid
        l = 0
        r = len(matrix[row])
        mid = (l+r)//2
        while(l<r):
            mid = (l+r)//2
            if(matrix[row][mid] == target): return True
            if(matrix[row][mid]>target):  r = mid
            else: l = mid+1

        return matrix[row][mid] == target