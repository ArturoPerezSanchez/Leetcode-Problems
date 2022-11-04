# https://leetcode.com/problems/construct-quad-tree

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def isLeaf(x, y, length):
            value = grid[x][y]
            for row in range(x, x + length):
                for col in range(y, y + length):
                    if grid[row][col] != value:
                        return False
            return True
        

        def rec(x, y, sideLength):
            if isLeaf(x, y, sideLength): return Node(grid[x][y], True, None, None, None, None)

            newNode = Node(0, False, None, None, None, None)
            length = int(sideLength/2)
            newNode.topLeft = rec(x, y, length)
            newNode.topRight = rec(x, y + length, length)
            newNode.bottomLeft = rec(x + length, y, length)
            newNode.bottomRight = rec(x + length, y + length, length)

            return newNode
        
        return rec(0, 0, len(grid))