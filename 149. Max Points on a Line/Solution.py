# https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)==1): return 1
        # Returns the parameters (m and n) of the equation of the line straight line (y = mx+n) that passes throught the given points
        def getLine(point_a, point_b):
            if(point_b[0]-point_a[0] == 0):
                return f'''{point_a[0]}'''
            m = round((point_b[1]-point_a[1])/(point_b[0]-point_a[0]),12)
            n = round(point_a[1]-m*point_a[0],12)
            return f'''{m}+{n}'''
        
        lines = {}
        for point_a_index in range(len(points)):
            for point_b_index in range(point_a_index+1, len(points)):
                line = getLine(points[point_a_index], points[point_b_index])
                if(line in lines):
                    lines[line].update([point_a_index, point_b_index])
                else:
                    lines[line] = set([point_a_index, point_b_index])
        return len(max(lines.values(),key=len))