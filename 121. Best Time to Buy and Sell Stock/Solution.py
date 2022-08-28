# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        biggest = prices[0]
        smallest = prices[0]
        for i in prices:
            if (i<smallest):
                smallest = i
                biggest = i
            elif(i>biggest):
                biggest=i
                res = max(res, biggest-smallest)

        return res