# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        aux = intervals[0]
        for i in range(1,len(intervals)):
            if(intervals[i][0] <= aux[1] and intervals[i][0] >= aux[0]):
                if (intervals[i][1] > aux[1]):
                    aux[1] = intervals[i][1]
            else:
                res.append(aux)
                aux = intervals[i]

        if(aux):
            res.append(aux)

        return res