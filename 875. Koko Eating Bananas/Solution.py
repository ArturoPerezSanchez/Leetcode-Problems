# https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1  
        while(l<r):
            mid = (l+r)//2
            if(sum([ceil(i/mid) for i in piles]) <= h): r = mid
            else: l = mid+1
        return r
