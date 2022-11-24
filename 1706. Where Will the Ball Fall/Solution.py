# https://leetcode.com/problems/where-will-the-ball-fall

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        res = list(range(n))
        if(n<=1): return [-1]
        for i in grid:
            for j in range(len(res)):
                if(res[j] != -1):
                    if(((res[j] == 0 and i[1] == -1) or (res[j] == n-1 and (i[n-1] == 1 or i[n-2] == 1))) or ((i[res[j]] == 1 and i[res[j]+1] == -1) or (i[res[j]] == -1 and i[res[j]-1] == 1))): res[j] = -1
                    else: res[j]+=i[res[j]]
        return res