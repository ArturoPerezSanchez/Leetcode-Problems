# https://leetcode.com/problems/maximum-subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        res = nums[0]
        for i in nums:
            counter += i
            if(counter>res):
                res = counter
            if(counter<0):
                counter = 0

        return res
        