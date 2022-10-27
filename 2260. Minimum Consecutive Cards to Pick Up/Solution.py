# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        res = -1
        for i in range(len(cards)):
            if(cards[i] in d):
                if(res== -1):
                    res =  i-d[cards[i]]+1
                else:
                    res=min(res, i-d[cards[i]]+1)

            d[cards[i]] = i
        return res
            
                
        