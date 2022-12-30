# https://leetcode.com/problems/jump-game-ii

class Solution:
        
    def jump(self, nums: List[int]) -> int:
        if(len(nums)<=1):return 0
        jumps = 0
        currentJumpEnd = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if(i==currentJumpEnd):
                jumps +=1
                currentJumpEnd = farthest
        return jumps

        