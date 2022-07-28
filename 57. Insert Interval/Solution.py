# https://leetcode.com/problems/insert-interval

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        def binSearch(val):
            l = 0
            r = len(intervals)
            while(l<r):
                mid = (l+r)//2
                if(val < intervals[mid][0]):
                    r = mid
                elif(val > intervals[mid][1]):
                    l = mid+1
                else:
                    break
            if not mid: mid = l
            return mid
        
        if(intervals[-1][1] < newInterval[0]):
            intervals.append(newInterval)
            return intervals

        start = binSearch(newInterval[0])
        if(intervals[start][1] < newInterval[0]): start+=1

        if(start >= len(intervals)):
            intervals.append(newInterval)
            return intervals

        if(intervals[start][0] > newInterval[0]):
            if(intervals[start][0] > newInterval[1]):
                intervals.insert(start, newInterval)
                return intervals
            else:
                intervals[start][0] = newInterval[0]
        
        end = binSearch(newInterval[1])
        if(end >= len(intervals)):
            intervals[-1][1] = newInterval[1]
            return intervals

        if(intervals[end][0] > newInterval[1]):
            intervals[start][1] = newInterval[1]
            i = start+1
            end = end-1
        else:
            intervals[start][1] = max(newInterval[1], intervals[end][1])

        i = start+1
        while(i<=end):
            intervals.pop(i)
            end-=1


        return intervals

