# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if(i in d): d.remove(i)
            else: d.add(i)
        return list(d)[0]

    def singleNumber2(self, nums: List[int]) -> int:
        if(len(nums) == 1): return nums[0]
        nums = sorted(nums)
        if(nums[0] != nums[1]): return nums[0]
        if(nums[-1] != nums[-2]): return nums[-1]
        for i in range(1, len(nums)-1):
            if(nums[i-1] != nums[i] and  nums[i+1] != nums[i]): return nums[i]
        return -1