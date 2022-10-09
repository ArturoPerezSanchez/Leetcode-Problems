# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = [0]
        res = 1
        for start, end in sorted(intervals):
            if(start < h[0]):
                heapq.heappush(h, end)
                res+=1
            else: heapq.heapreplace(h, end)
        return res