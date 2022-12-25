# https://leetcode.com/problems/find-missing-observations

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        nAvg = mean*(len(rolls) + n) - sum(rolls)

        if(nAvg/6>n or nAvg<n): return []
        res = []
        nAvg-=n
        for _ in range(n):
            if(nAvg - 5<=0):
                res.append(nAvg+1)
                break
            else:
                res.append(6)
                nAvg-=5
        
        if(len(res)<n):
            res +=[1]*(n-len(res))
        return res
