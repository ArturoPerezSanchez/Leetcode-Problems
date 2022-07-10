# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indl = 0
        indr = len(nums)-1
        while(indl<indr):
            val = nums[indl] + nums[indr]
            if(val<target):
                indl +=1
            elif(val>target):
                indr -=1
            else:
                return[indl+1, indr+1]