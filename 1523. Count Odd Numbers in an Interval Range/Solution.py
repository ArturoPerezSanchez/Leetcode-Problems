# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = int((high - low)/2)
        odds = ["1","3","5","7","9"]
        if(str(low)[-1] in odds or str(high)[-1] in odds): return res+1
        else: return res


