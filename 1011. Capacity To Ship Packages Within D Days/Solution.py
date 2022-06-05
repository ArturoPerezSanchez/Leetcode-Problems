# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = 0, 0
        for i in weights:
            r += i
            if(i>l): l=i
        
        def canShip(w):
            current_weight = 0
            current_day = 1
            for i in weights:
                current_weight +=i
                if(current_weight > w):
                    current_weight = i
                    current_day +=1
                if(current_day > days): return False
            return True

        while(l < r):
            mid = (l+r)//2
            if(canShip(mid)): r = mid
            else: l=mid+1
        return l

        