# https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[] for i in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res[col].append(matrix[row][col])
        return res
