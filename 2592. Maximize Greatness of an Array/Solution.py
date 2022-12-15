# https://leetcode.com/problems/maximize-greatness-of-an-array

class Solution(object):
    def maximizeGreatness(self, nums):
        n = len(nums)
        nums_sorted = sorted(nums)
        currentNum = nums_sorted[0]
        currentCount = 0
        rem = 0
        res = 0
        for i in nums_sorted:
            if i == currentNum:
                currentCount += 1
            else:
                rem+=currentCount
                currentCount = 1
                currentNum = i
                
            if(rem > 0):
                rem-=1
                res+=1
            
            
        return res
        