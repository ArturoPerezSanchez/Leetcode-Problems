# https://leetcode.com/problems/minimum-time-difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        lowest = 60*24
        mindistance = 60*24
        minutes = []

        for point in timePoints:
            hours, mins = point.split(":")
            pointInMinutes = int(hours)*60 + int(mins)
            minutes.append(pointInMinutes)
            if(pointInMinutes<lowest): lowest = pointInMinutes
        
        lowest += 60*24
        minutes = sorted(minutes)
        minutes.append(lowest)

        for i in range(len(minutes)-1):
            mindistance = min(mindistance, minutes[i+1] - minutes[i])
        
        return mindistance