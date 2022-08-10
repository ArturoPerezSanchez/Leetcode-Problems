# https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        currentInd = 0
        res = 1
        for i in target:
            pos = source.find(i, currentInd)
            if(pos == -1):
                pos = source.find(i, 0)
                if(pos == -1): return -1
                res+=1
            currentInd = pos+1
        return res
            