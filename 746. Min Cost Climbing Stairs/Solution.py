# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursive with memoization
        def recursion(steps, cost):
            global d
            if(steps in d): return d[steps]

            d[steps] = min(recursion(steps-1, cost), recursion(steps-2,cost)) + cost[-steps]
            return d[steps]
        global d
        d = {1:cost[-1], 2:cost[-2]}
        a = recursion(len(cost), cost)
        b = recursion(len(cost)-1, cost)
        return min(a, b)