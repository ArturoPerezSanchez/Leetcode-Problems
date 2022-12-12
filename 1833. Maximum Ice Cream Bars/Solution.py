# https://leetcode.com/problems/maximum-ice-cream-bars

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        for i in sorted(costs):
            if(i<= coins):
                coins-=i
                total +=1
        return total