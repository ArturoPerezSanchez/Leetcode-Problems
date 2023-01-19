# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=[]
        for i in range(len(matrix)):
            m.append([j[i] for j in reversed(matrix)])
        for j in range(len(m)):
            matrix[j] = m[j]