# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nextk = {}
        
        for i in range(len(nums)):
            if(nums[i] in nextk and 0 < i - nextk[nums[i]] <= k):
                return True
            else:
                nextk[nums[i]] = i
        return False