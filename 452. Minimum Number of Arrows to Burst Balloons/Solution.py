# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        minPoints = 1
        current = points[0]
        for i in points[1:]:
            if(i[0]<=current[1]):
                if(i[1]<current[1]):
                    current = [i[0], i[1]]
            else:
                minPoints +=1
                current = i
        return minPoints