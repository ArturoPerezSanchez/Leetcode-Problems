# https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if(total%2): return False
        mid = total//2

        @cache
        def rec(currentind, rem):
            if(rem == 0): return True
            if(rem < 0 or currentind >= len(nums)-1): return False
            currentind +=1
            return rec(currentind, rem-nums[currentind]) or rec(currentind, rem)
        
        return rec(0, mid)
