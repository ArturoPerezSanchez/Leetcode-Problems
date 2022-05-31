# https://leetcode.com/problems/smallest-range-ii

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        low, upper = nums[0], nums[-1]
        res = upper - low
        for i in range(len(nums) - 1):
            res = min(res, max(upper-k, nums[i]+k) - min(low+k, nums[i+1]-k))
        return res