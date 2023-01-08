# https://leetcode.com/problems/search-insert-position

class Solution(object):
    def searchInsert(self, nums, target):
        lp = 0
        rp = len(nums)-1
        while(lp<=rp):
            mid = (rp+lp)//2
            if (nums[mid] < target): lp = mid+1
            elif(nums[mid] > target): rp = mid-1
            else: return mid
        return lp