# https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = m*x + n
        if (coordinates[0][0] - coordinates[1][0] == 0):
            for point in coordinates:
                if(point[0] != coordinates[0][0]):
                    return False
            return True
        m = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        n = coordinates[0][1] - m*coordinates[0][0]

        for point in coordinates:
            if(point[0]*m +n != point[1]):
                return False

        return True

        