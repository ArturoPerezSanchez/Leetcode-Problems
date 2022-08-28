# https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {}
        def rec(ind):
            if(arr[ind] == 0): return True
            if(ind in visited): return False
            
            visited[ind] = 1

            res = False
            if(ind>= arr[ind]):
                res += rec(ind-arr[ind])
            
            if(not res and arr[ind] + ind < len(arr)):
                res += rec(arr[ind] + ind)
            
            return res
        return rec(start)
