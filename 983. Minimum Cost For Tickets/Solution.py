# https://leetcode.com/problems/minimum-cost-for-tickets

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        d = {}

        def rec(currentCost, ind):
            if ind in d: return currentCost + d[ind]
            if ind >= len(days):
                return currentCost

            today = days[ind]

            newInd = ind+1
            aux1 = rec(currentCost+costs[0], newInd)

            while(newInd<len(days) and days[newInd]<today+7): newInd +=1
            aux2 = rec(currentCost+costs[1], newInd)

            while(newInd<len(days) and days[newInd]<today+30): newInd +=1
            aux3 = rec(currentCost+costs[2], newInd)

            res = min(aux1,aux2,aux3)
            d[ind] = min(aux1,aux2,aux3)-currentCost
            return res

        return rec(0, 0)
