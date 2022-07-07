# https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        for i in nums:
            count+=i
            res.append(count)
        return res