# https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        res=1
        for i in s:
            if i in d:
                res +=1
                d={i}
            else:
                d.add(i)
        return res