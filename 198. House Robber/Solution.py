# https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        d = {}

        def rec(ind):
            if(ind >= len(nums)): return 0
            if ind in d: return d[ind]

            res = nums[ind] + max(rec(ind+2), rec(ind+3))
            d[ind] = res
            return res
        
        return max(rec(0), rec(1))